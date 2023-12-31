#include <iostream>
#include <stdexcept>
#include <tuple>
#include <cmath>
#include <algorithm>
#include <memory>
#include <new>
#include <vector>

using namespace std;

const double pi (atan(1) * 4);
const double eps(pow(10,-10));

class Kugla {
private:
    double r;
    double x,y,z;
    
public:
    explicit Kugla(double r = 0){ 
        if(r < 0) throw domain_error("Ilegalan poluprecnik");
        Kugla::r = r; x = y = z = 0;
        }
     Kugla(double x, double y, double z, double r = 0){
        if(r < 0) throw domain_error("Ilegalan poluprecnik");
        Kugla::r = r; Kugla::x = x; Kugla::y = y; Kugla::z =z;
     }
    explicit Kugla(const tuple<double, double, double> &centar, double r = 0){
        if(r < 0) throw domain_error("Ilegalan poluprecnik");
        Kugla::r = r;   x = get<0>(centar); y = get<1>(centar); z = get<2>(centar);
    }
    double DajX() const { return x; }
    double DajY() const { return y; }
    double DajZ() const { return z; }
    tuple<double, double, double> DajCentar() const { return make_tuple(DajX(), DajY(), DajZ()); }
    double DajPoluprecnik() const { return r; }
    double DajPovrsinu() const { return 4 * pow(DajPoluprecnik(), 2) * pi; }
    double DajZapreminu() const { return (4/3) * pow(DajPoluprecnik(), 3) * pi; }
    
    Kugla &PostaviX(double x) { Kugla::x = x; return *this; }
    Kugla &PostaviY(double y) { Kugla::y = y; return *this; }
    Kugla &PostaviZ(double z) { Kugla::z = z; return *this; }
    Kugla &PostaviCentar(double x, double y, double z) { PostaviX(x); PostaviY(y); PostaviZ(z); return *this; }
    Kugla &PostaviCentar(const tuple<double, double, double> &centar) { 
        PostaviX( get<0>(centar) ); PostaviY( get<1>(centar) ); PostaviZ( get<2>(centar) );
        return *this;
    }
    Kugla &PostaviPoluprecnik(double r) { 
        if(r < 0) throw domain_error("Ilegalan poluprecnik"); 
        Kugla::r = r; return *this; 
    }
    
    
    void Ispisi() const {
        cout<<"{("<<x<<","<<y<<","<<z<<"),"<<r<<"}"<<endl;
    }
    void Transliraj(double delta_x, double delta_y, double delta_z){ 
        x += delta_x;   y += delta_y;   z += delta_z;
    }
    
    friend bool DaLiSuIdenticne(const Kugla &k1, const Kugla &k2);
    friend bool DaLiSuPodudarne(const Kugla &k1, const Kugla &k2);
    friend bool DaLiSuKoncentricne(const Kugla &k1, const Kugla &k2);
    friend bool DaLiSeDodirujuIzvana(const Kugla &k1, const Kugla &k2);
    friend bool DaLiSeDodirujuIznutra(const Kugla &k1, const Kugla &k2);
    friend bool DaLiSePreklapaju(const Kugla &k1, const Kugla &k2);
    friend bool DaLiSeSijeku(const Kugla &k1, const Kugla &k2);
    
    bool DaLiSadrzi(const Kugla &k) const {
        if(RastojanjeCentara(*this,k) + k.DajPoluprecnik() < Kugla::r) return true;
        return false;
    }
    friend double RastojanjeCentara(const Kugla &k1, const Kugla &k2);
};

bool DaLiSuIdenticne(const Kugla &k1, const Kugla &k2){
    double x(k1.DajPoluprecnik()), y(k2.DajPoluprecnik());
    if(k1.DajCentar() != k2.DajCentar() || abs(x - y) > eps * (abs(x) + abs(y))) return false;
    return true;
}
bool DaLiSuPodudarne(const Kugla &k1, const Kugla &k2){
     double x(k1.DajPoluprecnik()), y(k2.DajPoluprecnik());
    if(abs(x - y) > eps * (abs(x) + abs(y))) return false;
    return true;
}                                                                                   //|x − y| < ε (| x|+| y|)
bool DaLiSuKoncentricne(const Kugla &k1, const Kugla &k2){
    if(k1.DajCentar() != k2.DajCentar()) return false;
    return true;
}
bool DaLiSeDodirujuIzvana(const Kugla &k1, const Kugla &k2){
    double x(k1.DajPoluprecnik() + k2.DajPoluprecnik()), y(RastojanjeCentara(k1,k2));
    if(abs(x - y) < eps * (abs(x) + abs(y))) return true;
    return false;
}
bool DaLiSeDodirujuIznutra(const Kugla &k1, const Kugla &k2){
    double x(abs(k1.DajPoluprecnik() - k2.DajPoluprecnik())), y(RastojanjeCentara(k1,k2));
    if(abs(x + y) <  eps * (abs(x) + abs(y))) return true;
    return false;
}
bool DaLiSePreklapaju(const Kugla &k1, const Kugla &k2){
    if(RastojanjeCentara(k1,k2) + k1.DajPoluprecnik() < k2.DajPoluprecnik() || 
    RastojanjeCentara(k1,k2) + k2.DajPoluprecnik() < k1.DajPoluprecnik()) return true;
    return false;
    }
bool DaLiSeSijeku(const Kugla &k1, const Kugla &k2){
    if(RastojanjeCentara(k1,k2) < k1.DajPoluprecnik() + k2.DajPoluprecnik() && RastojanjeCentara(k1,k2) + k1.DajPoluprecnik() > k2.DajPoluprecnik() 
    && RastojanjeCentara(k1,k2) + k2.DajPoluprecnik() > k1.DajPoluprecnik()) return true;
    return false;
}
double RastojanjeCentara(const Kugla &k1, const Kugla &k2){
    double t1;
    t1 = sqrt( pow(k1.DajX() - k2.DajX(), 2) + pow(k1.DajY() - k2.DajY(), 2) + pow(k1.DajZ() - k2.DajZ(), 2) );
    return t1;
}

int main ()
{
    
    try{
        
    cout<<"Unesite broj kugla: ";
    int n;
    cin>>n;
    while(!cin || n <= 0){
        cin.clear();
        cin.ignore(1000, '\n');
        cout<<"Neispravan broj kugli, unesite ponovo!"<<endl;
        cin>>n;
    }
    
    vector <shared_ptr<Kugla>> vek;
    
    for(int i = 0; i < n; i++){
        double x,y,z;
        double r;
        
        cout<<"Unesite centar "<< i + 1 <<". kugle: ";
        cin>>x>>y>>z;
        while(!cin) {
            cin.clear();
            cin.ignore(1000, '\n');
            cout<<"Neispravan centar"<<endl;
            cout<<"Unesite centar "<< i + 1 <<". kugle: ";
            cin>>x>>y>>z;
        }
        tuple<double, double, double> temp(make_tuple(x,y,z));
        
        cout<<"Unesite poluprecnik "<< i + 1 <<". kugle: ";
        cin>>r;
        if(!cin) {
            cin.clear();
            cin.ignore(1000, '\n');
            cout<<"Ilegalan poluprecnik"<<endl;
            i--;
            continue;
        }
        
        try{
            shared_ptr<Kugla> p(make_shared<Kugla>(temp,r));
             vek.push_back(p);
        }
        catch(domain_error e){
            i--;
            cout<<e.what()<<endl;
        }
    }
    
        cout<<"Unesite parametre translacije (delta_x,delta_y,delta_z): ";
        int delta_z, delta_y, delta_x;
        cin>>delta_x>>delta_y>>delta_z;
        while(!cin){
            cin.clear();
            cin.ignore(1000, '\n');
            cout<<"Neispravni parametri translacije, unesite ponovo!"<<endl;
            cin>>delta_x>>delta_y>>delta_z;
        }
        
       transform(vek.begin(), vek.end(), vek.begin(), [delta_x, delta_y, delta_z] ( shared_ptr<Kugla> &k1){ k1->Transliraj(delta_x, delta_y, delta_z); return k1; } );
        
        cout<<"Kugle nakon obavljenje transformacije imaju sljedece vrijednosti: "<<endl;
        
        sort(vek.begin(), vek.end(), [] (const shared_ptr<Kugla> &k1, const shared_ptr<Kugla> &k2) {
            if(k1->DajZapreminu() < k2->DajZapreminu()) return true;
            return false;
        });
        for_each(vek.begin(), vek.end(), [](const shared_ptr<Kugla> &k) {    k->Ispisi();   });
        
        cout<<"Kugla sa najvecom povrsinom je: ";
        
        auto p =max_element(vek.begin(), vek.end(), [] (const shared_ptr<Kugla> &k1, const shared_ptr<Kugla> &k2){
            if(k1->DajPovrsinu() < k2->DajPovrsinu()) return true;
            return false;
        }); 
        (*p)->Ispisi();
        
        int br = 0;
        int i = 0;
        for_each(vek.begin(), vek.end(), [&i, &br, vek] (const shared_ptr<Kugla> &k1){
            i++;
            for_each(vek.begin() + i, vek.end(), [i, &br,k1] (const shared_ptr<Kugla> &k2){
                if(DaLiSeSijeku(*k1,*k2)) { 
                    br++;
                    cout<<"Presjecaju se kugle: ";
                    k1->Ispisi(); k2->Ispisi();
                }
            });
        });
        if(br == 0) cout<<"Ne postoje kugle koje se presjecaju!";
    }
    catch(domain_error e){
        cout<<e.what()<<endl;
    }
 
        
	return 0;
	
}
