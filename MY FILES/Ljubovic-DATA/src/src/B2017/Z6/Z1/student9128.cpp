#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
#include <algorithm>
#include <memory>
#include <fstream>

using std::cout;
using std::cin;

class Spremnik {
protected:
    double tezina_spremnika;
    std::string naziv_sadrzaja;
public: 
    Spremnik(double tez, std::string ime) : tezina_spremnika(tez), naziv_sadrzaja(ime) {};
    double DajTezinu() const {return tezina_spremnika;}
    virtual double DajUkupnuTezinu() const = 0;
    virtual void Ispisi() const = 0;
    virtual ~Spremnik(){};
    virtual std::shared_ptr<Spremnik> DajKopiju() const = 0;
};

class Sanduk : public Spremnik {
    std::vector<double> tezina_po_predmetu;
public: 
    Sanduk(double, std::string, std::vector<double>);
    double DajUkupnuTezinu() const;
    void Ispisi() const;
    friend class Skladiste;
    ~Sanduk(){}
    std::shared_ptr<Spremnik> DajKopiju() const {return std::make_shared<Sanduk>(Sanduk(tezina_spremnika, naziv_sadrzaja, tezina_po_predmetu));}
};

class Vreca : public Spremnik {
    double tezina_materije;
public: 
    Vreca(double tez_spr, std::string ime, double tez_mat);
    double DajUkupnuTezinu() const {return tezina_spremnika+tezina_materije;}
    void Ispisi() const;
    friend class Skladiste;
    std::shared_ptr<Spremnik> DajKopiju() const {return std::make_shared<Vreca>(Vreca(tezina_spremnika, naziv_sadrzaja, tezina_materije));}
};

class Bure : public Spremnik {
    double gustina_tecnosti;
    double zapremina;
public:
    Bure(double, std::string, double, double);
    double DajUkupnuTezinu() const {return tezina_spremnika+gustina_tecnosti*zapremina*(1e-3);}
    void Ispisi() const;
    friend class Skladiste;
    std::shared_ptr<Spremnik> DajKopiju() const {return std::make_shared<Bure>(Bure(tezina_spremnika, naziv_sadrzaja, gustina_tecnosti, zapremina));}
};

double Sanduk::DajUkupnuTezinu() const {
    double suma(0);
    for(int i : tezina_po_predmetu) suma+=i;
    return suma+tezina_spremnika;
}

Bure::Bure(double tez_spr, std::string ime, double gustina, double volumen) : Spremnik(tez_spr, ime), gustina_tecnosti(gustina), zapremina(volumen) {}
Vreca::Vreca(double tez_spr, std::string ime, double tez_mat) : Spremnik(tez_spr, ime), tezina_materije(tez_mat) {}
Sanduk::Sanduk(double tez_spr, std::string ime, std::vector<double> vektor_tezina) : Spremnik(tez_spr, ime) {
    tezina_po_predmetu.resize(vektor_tezina.size());
    std::copy(vektor_tezina.begin(), vektor_tezina.end(), tezina_po_predmetu.begin());
}

void Sanduk::Ispisi() const {
    cout<<"Vrsta spremnika: Sanduk"<<std::endl;
    cout<<"Sadrzaj: "<<naziv_sadrzaja<<std::endl;
    cout<<"Tezine predmeta: "; for(auto i : tezina_po_predmetu) cout<<i<<" "; cout<<"(kg)"<<std::endl;
    cout<<"Vlastita tezina: "<<tezina_spremnika<<" (kg)"<<std::endl;
    cout<<"Ukupna tezina: "<<DajUkupnuTezinu()<<" (kg)"<<std::endl;
}

void Bure::Ispisi() const {
    cout<<"Vrsta spremnika: Bure"<<std::endl;
    cout<<"Sadrzaj: "<<naziv_sadrzaja<<std::endl;
    cout<<"Vlastita tezina: "<<tezina_spremnika<<" (kg)"<<std::endl;
    cout<<"Specificna tezina tecnosti: "<<gustina_tecnosti<<" (kg/m^3)"<<std::endl;
    cout<<"Zapremina tecnosti: "<<zapremina<<" (l)"<<std::endl;
    cout<<"Ukupna tezina: "<<DajUkupnuTezinu()<<" (kg)"<<std::endl;
}

void Vreca::Ispisi() const {
    cout<<"Vrsta spremnika: Vreca"<<std::endl;
    cout<<"Sadrzaj: "<<naziv_sadrzaja<<std::endl;
    cout<<"Vlastita tezina: "<<tezina_spremnika<<" (kg)"<<std::endl;
    cout<<"Tezina pohranjene materije: "<<tezina_materije<<" (kg)"<<std::endl;
    cout<<"Ukupna tezina: "<<DajUkupnuTezinu()<<" (kg)"<<std::endl;
}

class Skladiste {
    std::vector<std::shared_ptr<Spremnik>> vektor;
public: 
    Skladiste() = default;
    Skladiste(const Skladiste &s);
    Skladiste(Skladiste &&s);
    Skladiste &operator =(Skladiste s);
    Spremnik *DodajSanduk(double tez_spr, std::string ime, std::vector<double> vektor_tezina);
    Spremnik *DodajVrecu(double tez_spr, std::string ime, double tez_mat);
    Spremnik *DodajBure(double tez_spr, std::string ime, double gustina, double volumen);
    Spremnik *DodajSpremnik(Spremnik *objekat, bool cuvati);
    void BrisiSpremnik(Spremnik *brisat);
    Spremnik &DajNajtezi();
    Spremnik &DajNajlaksi();
    int BrojPreteskih(int) const;
    void IzlistajSkladiste() const;
    void UcitajIzDatoteke(const std::string &ime_dat);
};

void Skladiste::UcitajIzDatoteke(const std::string &ime_dat) {
    std::ifstream ulaz(ime_dat);
    if(!ulaz) throw std::logic_error("Trazena datoteka ne postoji");
    this->vektor.resize(0);
    
    char koja_vrsta, pomocni;
    std::string naziv;
    
    for(;;) {
        koja_vrsta=ulaz.get();
        if(koja_vrsta=='S') {
            ulaz>>std::ws;
            if(!ulaz && !ulaz.eof()) throw std::logic_error("Problemi pri citanju datoteke");
            if(ulaz.eof()) throw std::logic_error("Datoteka sadrzi besmislene podatke");
            std::getline(ulaz, naziv);
            if(!ulaz && !ulaz.eof()) throw std::logic_error("Problemi pri citanju datoteke");
            if(ulaz.eof()) throw std::logic_error("Datoteka sadrzi besmislene podatke");
            double tezina_sanduka;
            ulaz>>tezina_sanduka;
            if(!ulaz && !ulaz.eof()) throw std::logic_error("Problemi pri citanju datoteke");
            if(ulaz.eof()) throw std::logic_error("Datoteka sadrzi besmislene podatke");
            int koliko_clanova;
            ulaz>>koliko_clanova;
            if(!ulaz && !ulaz.eof()) throw std::logic_error("Problemi pri citanju datoteke");
            if(ulaz.eof()) throw std::logic_error("Datoteka sadrzi besmislene podatke");
            std::vector<double> clanovi(koliko_clanova);
            int i;
            for(i=0; i<koliko_clanova; i++) {
                ulaz>>clanovi[i];
                if(!ulaz && !ulaz.eof()) throw std::logic_error("Datoteka sadrzi besmislene podatke");
                if(ulaz.eof()) break;
                while(ulaz.peek()==' ') ulaz.get();
                if(ulaz.peek()=='\n') break;
            }
            if(i<koliko_clanova-1) throw std::logic_error("Datoteka sadrzi besmislene podatke");
            vektor.emplace_back(std::make_shared<Sanduk>(Sanduk(tezina_sanduka, naziv, clanovi)));
            ulaz>>std::ws;
            
        } else if(koja_vrsta=='B') {
            ulaz>>std::ws;
            if(!ulaz && !ulaz.eof()) throw std::logic_error("Problemi pri citanju datoteke");
            if(ulaz.eof()) throw std::logic_error("Datoteka sadrzi besmislene podatke");
            std::getline(ulaz, naziv);
            if(!ulaz && !ulaz.eof()) throw std::logic_error("Problemi pri citanju datoteke");
            if(ulaz.eof()) throw std::logic_error("Datoteka sadrzi besmislene podatke");
            double tezina_bureta, gustina, zapremina;
            ulaz>>tezina_bureta>>gustina>>zapremina;
            if(!ulaz && !ulaz.eof()) throw std::logic_error("Problemi pri citanju datoteke");
            vektor.emplace_back(std::make_shared<Bure>(Bure(tezina_bureta, naziv, gustina, zapremina)));
            ulaz>>std::ws;
            
        } else if(koja_vrsta=='V') {
            ulaz>>std::ws;
            if(!ulaz && !ulaz.eof()) throw std::logic_error("Problemi pri citanju datoteke");
            if(ulaz.eof()) throw std::logic_error("Datoteka sadrzi besmislene podatke");
            std::getline(ulaz, naziv);
            if(!ulaz && !ulaz.eof()) throw std::logic_error("Problemi pri citanju datoteke");
            if(ulaz.eof()) throw std::logic_error("Datoteka sadrzi besmislene podatke");
            double tezina_vrece, tezina_materije;
            ulaz>>tezina_vrece>>tezina_materije;
            if(!ulaz && !ulaz.eof()) throw std::logic_error("Problemi pri citanju datoteke");
            vektor.emplace_back(std::make_shared<Vreca>(Vreca(tezina_vrece, naziv, tezina_materije)));
            ulaz>>std::ws;
        } else throw std::logic_error("Datoteka sadrzi besmislene podatke");
        if(ulaz.eof()) break;
    }
}

void Skladiste::IzlistajSkladiste() const {
    auto ispis(vektor);
    std::sort(ispis.begin(), ispis.end(), [](std::shared_ptr<Spremnik> s1, std::shared_ptr<Spremnik> s2) {return s1->DajUkupnuTezinu()>s2->DajUkupnuTezinu();});
    for (auto i : ispis) {
        i->Ispisi();
    }
}
Skladiste::Skladiste(const Skladiste &s) {
    vektor.resize(s.vektor.size());
    for(int i=0; i<vektor.size(); i++) vektor[i] = s.vektor[i]->DajKopiju();
}

Skladiste::Skladiste(Skladiste &&s) : vektor(s.vektor) {}

Skladiste &Skladiste::operator =(Skladiste s) {
    std::swap(vektor, s.vektor);
    return *this;
}

Spremnik *Skladiste::DodajSanduk(double tez_spr, std::string ime, std::vector<double> vektor_tezina) {
    vektor.emplace_back(std::make_shared<Sanduk>(Sanduk(tez_spr, ime, vektor_tezina)));
    return vektor[vektor.size()-1].get();
   // return (std::static_pointer_cast<std::shared_ptr<Spremnik>>(vektor[vektor.size()-1])).get();
    
}

Spremnik *Skladiste::DodajVrecu(double tez_spr, std::string ime, double tez_mat) {
    vektor.emplace_back(std::make_shared<Vreca>(Vreca(tez_spr, ime, tez_mat)));
    return vektor[vektor.size()-1].get();
}

Spremnik *Skladiste::DodajBure(double tez_spr, std::string ime, double gustina, double volumen) {
    vektor.emplace_back(std::make_shared<Bure>(Bure(tez_spr, ime, gustina, volumen)));
    return vektor[vektor.size()-1].get();
}

Spremnik *Skladiste::DodajSpremnik(Spremnik *objekat, bool cuvati) {
    if(cuvati) {
        vektor.emplace_back(objekat);
        objekat=nullptr;
        return vektor[vektor.size()-1].get();
    } else {
        vektor.emplace_back(objekat->DajKopiju());
        return vektor[vektor.size()-1].get();
    }
}

void Skladiste::BrisiSpremnik(Spremnik *brisat) {
    for(int i=0; i<vektor.size(); i++) {
        if(brisat==vektor[i].get()) {
            vektor[i]=nullptr;
            vektor.erase(vektor.begin()+i);
            break;
        }
    }
}

Spremnik &Skladiste::DajNajtezi() {
    if(vektor.empty()) throw std::range_error("Skladiste je prazno");
    return **std::max_element(vektor.begin(), vektor.end(), [](std::shared_ptr<Spremnik> s1, std::shared_ptr<Spremnik> s2) {return s2->DajTezinu()>s1->DajTezinu();});
}

Spremnik &Skladiste::DajNajlaksi() {
    if(vektor.empty()) throw std::range_error("Skladiste je prazno");
    return **std::min_element(vektor.begin(), vektor.end(), [](std::shared_ptr<Spremnik> s1, std::shared_ptr<Spremnik> s2) {return s1->DajTezinu()<s2->DajTezinu();});
}

int Skladiste::BrojPreteskih(int broj_preteskih) const {
    auto broj=std::count_if(vektor.begin(), vektor.end(), [broj_preteskih](std::shared_ptr<Spremnik> s) {return s->DajUkupnuTezinu()>double(broj_preteskih);});
    return broj;
}

int main ()
{
    Skladiste s;
    
    try {
        s.UcitajIzDatoteke("ROBA.TXT");
        s.IzlistajSkladiste();
    } catch(const std::exception &e) {
        cout<<e.what();
    }
	return 0;
}
