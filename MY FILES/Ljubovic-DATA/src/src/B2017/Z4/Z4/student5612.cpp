#include <iostream>
#include <tuple>
#include <stdexcept>
#include <utility>
#include <iomanip>
#include <initializer_list>
#include <algorithm>
#include <string>
#include <memory>
#include <vector>

//KLASA Datum
class Datum
{
    int dan, mjesec, godina;
public:
    //Deklaracija i implementacija konstruktora
    Datum(int dan, int mjesec, int godina) {
        Postavi(dan,mjesec,godina);
    }
    //Deklaracija i implementacija metode Postavi
    void Postavi(int dan, int mjesec, int godina) {
        int broj_dana[] {31,28,31,30,31,30,31,31,30,31,30,31};
        if(godina % 4 == 0 && (godina % 100 != 0 || godina % 400 == 0)) broj_dana[1]++;
        if(godina < 1 || mjesec < 1 || mjesec > 12 || dan < 1 || dan > broj_dana[mjesec-1])
            throw std::domain_error("Neispravan datum");

        Datum::dan = dan;
        Datum::mjesec = mjesec;
        Datum::godina = godina;
    }
    //Deklaracija i implementacija metode Ocitaj
    std::tuple<int, int, int> Ocitaj() const {
        return std::make_tuple(dan,mjesec,godina);
    }
    //Deklaracija i implementacija metode Ispisi
    void Ispisi() const {
        std::cout << dan << "/" << mjesec << "/" << godina;
    }
};
//KLASA Vrijeme
class Vrijeme
{
    int sati, minute;
public:
    //Deklaracija i implementacija Konstruktora
    Vrijeme(int sati, int minute) {
        Postavi(sati, minute);
    }
    //Deklaracija i implementacija metode Postavi
    void Postavi(int sati, int minute) {
        if(sati < 0 || sati > 23 || minute < 0 || minute > 59) throw std::domain_error("Neispravno vrijeme");
        Vrijeme::sati = sati;
        Vrijeme::minute = minute;
    }
    //Deklaracija i implementacija metode Ocitaj
    std::pair<int, int> Ocitaj() const {
        return std::make_pair(sati,minute);
    }
    //Deklaracija i implementacija metode Ispisi
    void Ispisi() const {
        std::cout << std::setw(2) << std::right << std::setfill('0') << sati << ":" << std::setw(2)
                  << std::right << std::setfill('0') << minute;
    }
};

//KLASA Pregled
class Pregled
{
    std::string ime_pacijenta;
    Datum datum_pregleda {1,1,2000};
    Vrijeme vrijeme_pregleda {0,0};
public:
    //Deklaracija i implementacija konstruktora
    Pregled(const std::string &Ime_pacijenta, const Datum &Datum_pregleda, const Vrijeme &Vrijeme_pregleda) {
        datum_pregleda = Datum_pregleda;
        vrijeme_pregleda = Vrijeme_pregleda;
        ime_pacijenta = Ime_pacijenta;
    }
    //Deklaracija i implementacija konstruktora
    Pregled(const std::string &Ime_pacijenta, int dan_pregleda, int mjesec_pregleda, int godina_pregleda,
            int sati_pregleda, int minute_pregleda):
        datum_pregleda(dan_pregleda,mjesec_pregleda,godina_pregleda),
        vrijeme_pregleda(sati_pregleda,minute_pregleda) {
        ime_pacijenta = Ime_pacijenta;
    }
    //Deklaracija metode PromijeniPacijenta
    void PromijeniPacijenta(const std::string &ime_pacijenta);

    //Deklaracija metode PromijeniDatum
    void PromijeniDatum(const Datum &novi_datum);

    //Deklaracija metode PromijeniVrijeme
    void PromijeniVrijeme(const Vrijeme &novo_vrijeme);

    //Deklaracija metode PomjeriDanUnaprijed
    void PomjeriDanUnaprijed();

    //Deklaracija metode PomjeriDanUnazad
    void PomjeriDanUnazad();

    //Deklaracija metode DajImePacijenta
    std::string DajImePacijenta() const;

    //Deklaracija metode DajDatumPregleda
    Datum DajDatumPregleda() const;

    //Deklaracija metode DajVrijemePregleda
    Vrijeme DajVrijemePregleda() const;

    //Deklaracija i implementacija metode DolaziPrije
    static bool DolaziPrije(const Pregled &p1, const Pregled &p2) {
        if(std::get<2>(p1.DajDatumPregleda().Ocitaj()) < std::get<2>(p2.DajDatumPregleda().Ocitaj())) return true;
        else if(std::get<2>(p1.DajDatumPregleda().Ocitaj()) > std::get<2>(p2.DajDatumPregleda().Ocitaj())) return false;
        else {
            if(std::get<1>(p1.DajDatumPregleda().Ocitaj()) < std::get<1>(p2.DajDatumPregleda().Ocitaj())) return true;
            else if(std::get<1>(p1.DajDatumPregleda().Ocitaj()) > std::get<1>(p2.DajDatumPregleda().Ocitaj())) return false;
            else {
                if(std::get<0>(p1.DajDatumPregleda().Ocitaj()) < std::get<0>(p2.DajDatumPregleda().Ocitaj())) return true;
                else if(std::get<0>(p1.DajDatumPregleda().Ocitaj()) > std::get<0>(p2.DajDatumPregleda().Ocitaj())) return false;
                else {
                    if(std::get<0>(p1.DajVrijemePregleda().Ocitaj()) < std::get<0>(p2.DajVrijemePregleda().Ocitaj())) return true;
                    else if(std::get<0>(p1.DajVrijemePregleda().Ocitaj()) > std::get<0>(p2.DajVrijemePregleda().Ocitaj())) return false;
                    else {
                        if(std::get<1>(p1.DajVrijemePregleda().Ocitaj()) < std::get<1>(p2.DajVrijemePregleda().Ocitaj())) return true;
                    }
                }
            }
        }
        return false;
    }

    //Deklaracija metode Ispisi
    void Ispisi() const;
};
//Implementacija metode PromijeniPacijenta
void Pregled::PromijeniPacijenta(const std::string &ime_pacijenta)
{
    Pregled::ime_pacijenta = ime_pacijenta;
}
//Implementacija metode PromijeniDatum
void Pregled::PromijeniDatum(const Datum &novi_datum)
{
    Pregled::datum_pregleda = novi_datum;
}
//Implementacija metode PromijeniVrijeme
void Pregled::PromijeniVrijeme(const Vrijeme &novo_vrijeme)
{
    Pregled::vrijeme_pregleda = novo_vrijeme;
}
//Implementacija metode PomjeriDanUnaprijed
void Pregled::PomjeriDanUnaprijed()
{
    int broj_dana[] {31,28,31,30,31,30,31,31,30,31,30,31};
    int d, m, g;
    std::tie(d, m, g) = datum_pregleda.Ocitaj();
    if(g % 4 == 0 && (g & 100 != 0 || g % 400 == 0)) broj_dana[1]++;
    d++;
    if(d > broj_dana[m-1]) {
        m++;
        d = 1;
    }
    if(m > 12) {
        m = 1;
        g++;
    }
}
//Implementacija metode PomjeriDanUnazad
void Pregled::PomjeriDanUnazad()
{
    int broj_dana[] {31,28,31,30,31,30,31,31,30,31,30,31};
    int d, m, g;
    std::tie(d, m, g) = datum_pregleda.Ocitaj();
    if(g % 4 == 0 && (g % 100 != 0 || g % 400 == 0)) broj_dana[1]++;
    d--;
    if(d <= 0) {
        m--;
        d = broj_dana[m-1];
    }
    if(m < 1) {
        m = 12;
        g--;
    }
}
//Implementacija metode DajImePacijenta
std::string Pregled::DajImePacijenta() const
{
    return ime_pacijenta;
}
//Implementacija metode DajDatumPregleda
Datum Pregled::DajDatumPregleda() const
{
    return datum_pregleda;
}
//Implementacija metode DajVrijemePregleda
Vrijeme Pregled::DajVrijemePregleda() const
{
    return vrijeme_pregleda;
}
//Implementacija metode Ispisi
void Pregled::Ispisi() const
{
    std::cout << std::setw(30) << std::left << std::setfill(' ') << ime_pacijenta;
    datum_pregleda.Ispisi();
    std::cout << " ";
    vrijeme_pregleda.Ispisi();
    std::cout << std::endl;
}
//KLASA Pregledi
class Pregledi
{
    int broj_pregleda;
    std::vector<std::shared_ptr<Pregled>> V;
public:
    //Deklaracija i implementacija konstruktora
    explicit Pregledi():broj_pregleda(0) {}

    //Deklaracija sekvencijskog konstruktora
    Pregledi(std::initializer_list<Pregled> spisak_pregleda);

    //Deklaracija destruktora
    //~Pregledi();

    //Deklaracija kopirajuceg konstruktora
    //Pregledi(const Pregledi &pregledi);

    //Deklaracija pomjerajuceg konstruktora
    //Pregledi(Pregledi &&pregledi);

    //Deklaracija kopirajuceg operatora dodjele
    //Pregledi &operator = (const Pregledi &pregledi);

    //Deklaracija pomjerajuceg operatora dodjele
    //Pregledi &operator = (Pregledi &&pregledi);

    //Deklaracija metode RegistrirajPregled
    void RegistrirajPregled(const std::string &ime_pacijenta, const Datum &datum_pregleda, const Vrijeme &vrijeme_pregleda);

    //Deklaracija metode RegistrirajPregled
    void RegistrirajPregled(const std::string &ime_pacijenta, int dan_pregleda, int mjesec_pregleda, int godina_pregleda,
                            int sati_pregleda,int minute_pregleda);

    //Deklaracija metode RegistrirajPregled
    void RegistrirajPregled(std::shared_ptr<Pregled> pregled);

    //Deklaracija metode DajBrojPregleda
    int DajBrojPregleda() const;

    //Deklaracija metode DajBrojPregledaNaDatum
    int DajBrojPregledaNaDatum(const Datum &datum) const;

    //Deklaracija metode DajNajranijiPregled
    Pregled &DajNajranijiPregled();

    //Deklaracija metode DajNajranijiPregled
    Pregled DajNajranijiPregled() const;

    //Deklaracija metode IsprazniKolekciju
    void IsprazniKolekciju();

    //Deklaracija metode ObrisiNajranijiPregled
    void ObrisiNajranijiPregled();

    //Deklaracija metode ObrisiPregledePacijenata
    void ObrisiPregledePacijenata(const std::string &ime_pacijenta);

    //Deklaracija metode IspisiPregledeNaDatum
    void IspisiPregledeNaDatum(const Datum &datum) const;

    //Deklaracija metode IspisiSvePreglede
    void IspisiSvePreglede() const;


    //Deklaracija i implementacija kopirajuceg konstruktora
    Pregledi(const Pregledi &pregledi):broj_pregleda(pregledi.broj_pregleda) {
        try {
            V.resize(pregledi.broj_pregleda);
            try {
                for(int i = 0; i < pregledi.broj_pregleda; i++) {
                    V[i] = std::shared_ptr<Pregled>(0);
                }
            } catch(...) {
                throw;
            }
        } catch(...) {
            throw;
        }
    }
    //Deklaracija i implementacija pomjerajuceg konstruktora
    Pregledi(Pregledi &&pregledi):broj_pregleda(pregledi.broj_pregleda),V(pregledi.broj_pregleda) {
        pregledi.broj_pregleda = 0;
        pregledi.V.resize(pregledi.broj_pregleda);
    }

    //Deklaracija i implementacija kopirajuceg operatora dodjele
    Pregledi &operator = (const Pregledi &pregledi) {
        if(broj_pregleda > pregledi.broj_pregleda) {
            for(int i = pregledi.broj_pregleda; i < broj_pregleda; i++) {
                V[i] = nullptr;
            }
        } else {
            try {
                std::vector<std::shared_ptr<Pregled>> novi_prostor(pregledi.broj_pregleda);
                for(int i = 0; i < broj_pregleda; i++) {
                    V[i] = nullptr;
                }
                V = novi_prostor;
            } catch(...) {
                throw;
            }
        }
        broj_pregleda = pregledi.broj_pregleda;
        for(int i = 0; i < broj_pregleda; i++) {
            *V[i] = *pregledi.V[i];
        }
        return *this;
    }
    //Deklaracija i implementacija pomjerajuceg operatora dodjele
    Pregledi &operator =(Pregledi &&pregledi) {
        std::swap(broj_pregleda, pregledi.broj_pregleda);
        std::swap(V,pregledi.V);
        return *this;
    }
};

//Implementacija sekvencijskog konstruktora
Pregledi::Pregledi(std::initializer_list<Pregled> spisak_pregleda):
    broj_pregleda(spisak_pregleda.size())
{
    for(int i = 0; i < broj_pregleda; i++) {
        V[i] = std::make_shared<Pregled>(spisak_pregleda.begin()[i]);
    }
}

//Implementacija metode RegistrirajPregled
void Pregledi::RegistrirajPregled(const std::string &ime_pacijenta, const Datum &datum_pregleda, const Vrijeme &vrijeme_pregleda)
{
    V.resize(broj_pregleda + 1);
    V[broj_pregleda++] = std::make_shared<Pregled>(ime_pacijenta,datum_pregleda,vrijeme_pregleda);
}
//Implementacija metode RegistrirajPregled
void Pregledi::RegistrirajPregled(const std::string &ime_pacijenta, int dan_pregleda, int mjesec_pregleda, int godina_pregleda,
                                  int sati_pregleda, int minute_pregleda)
{
    V.resize(broj_pregleda+1);
    V[broj_pregleda] = std::make_shared<Pregled>(ime_pacijenta,dan_pregleda,mjesec_pregleda,godina_pregleda,sati_pregleda,minute_pregleda);
    broj_pregleda++;
}
//Implementacija metode RegistrirajPregled
void Pregledi::RegistrirajPregled(std::shared_ptr<Pregled> pregled)
{
    V.resize(broj_pregleda + 1);
    V[broj_pregleda++] = pregled;
}
//Implementacija metode DajBrojPregleda
int Pregledi::DajBrojPregleda() const
{
    return broj_pregleda;
}

//Implementacija metode DajBrojPregledaNaDatum
int Pregledi::DajBrojPregledaNaDatum(const Datum &datum) const
{
    int broj = std::count_if(V.begin(),V.end(),[datum](std::shared_ptr<Pregled> pok) {
        return (std::get<0>(datum.Ocitaj()) == std::get<0>(pok->DajDatumPregleda().Ocitaj()) &&
                std::get<1>(datum.Ocitaj()) == std::get<1>(pok->DajDatumPregleda().Ocitaj()) &&
                std::get<2>(datum.Ocitaj()) == std::get<2>(pok->DajDatumPregleda().Ocitaj()));
    });
    return broj;
}

//Implementacija metode DajNajranijiPregled
Pregled &Pregledi::DajNajranijiPregled()
{
    if(broj_pregleda == 0) throw std::domain_error("Nema registriranih pregleda");
    return (**(std::min_element(V.begin(),V.end(), [](std::shared_ptr<Pregled> p1, std::shared_ptr<Pregled> p2) {
        return (Pregled::DolaziPrije(*p1,*p2));
    })));
}

//Implementacija metode DajNajranijiPregled
Pregled Pregledi::DajNajranijiPregled() const
{
    return (**(std::min_element(V.begin(),V.end(),[](std::shared_ptr<Pregled> p1, std::shared_ptr<Pregled> p2) {
        return (Pregled::DolaziPrije(*p1,*p2));
    })));
}

//Implementacija metode IsprazniKolekciju

//Implementacija metode ObrisiNajranijiPregled
void Pregledi::ObrisiNajranijiPregled()
{
    if(broj_pregleda == 0) throw std::range_error("Prazna kolekcija");
    for(int i = 0; i < broj_pregleda; i++) {
        if(std::get<0>(V[i]->DajDatumPregleda().Ocitaj()) == std::get<0>(DajNajranijiPregled().DajDatumPregleda().Ocitaj()) &&
                std::get<1>(V[i]->DajDatumPregleda().Ocitaj()) == std::get<1>(DajNajranijiPregled().DajDatumPregleda().Ocitaj()) &&
                std::get<2>(V[i]->DajDatumPregleda().Ocitaj()) == std::get<2>(DajNajranijiPregled().DajDatumPregleda().Ocitaj())) {
            std::swap(V[i],V[broj_pregleda-1]);
            broj_pregleda--;
            V.resize(broj_pregleda);
            break;
        }
    }
}

//Implementacija metode ObrisiPregledePacijenata
void Pregledi::ObrisiPregledePacijenata(const std::string &ime_pacijenta)
{
    for(int i = 0; i < broj_pregleda; i++) {
        if(V[i]->DajImePacijenta() == ime_pacijenta) {
            std::swap(V[i],V[broj_pregleda-1]);
            broj_pregleda--;
            V.resize(broj_pregleda);
        }
    }
}

//Implementacija metode IspisiPregledeNaDatum
void Pregledi::IspisiPregledeNaDatum(const Datum &datum) const
{
    for(int i = 0; i < broj_pregleda; i++) {
        if(std::get<0>(V[i]->DajDatumPregleda().Ocitaj()) == std::get<0>(datum.Ocitaj()) &&
                std::get<1>(V[i]->DajDatumPregleda().Ocitaj()) == std::get<1>(datum.Ocitaj()) &&
                std::get<2>(V[i]->DajDatumPregleda().Ocitaj()) == std::get<2>(datum.Ocitaj()))
            V[i]->Ispisi();
    }
}

//Implementacija metode IspisiSvePreglede
void Pregledi::IspisiSvePreglede() const
{
    if(V.size() == 0) return;
    std::vector<int> Pozicije(V.size());
    int j(0);
    while(j < V.size()) {
        int index(0);
        int i(0);
        while(i < V.size()) {
            if(i == j) {
                i++;
                continue;
            }
            if(Pregled::DolaziPrije(*V[j],*V[i]) == false) index++;
            i++;
        }
        Pozicije[index] = j;
        j++;
    }
    int k(0);
    while(k < V.size()) {
        V[Pozicije[k]]->Ispisi();
        k++;
    }
}

int main ()
{
    int broj_pregleda(0);
    std::string name;
    std::string kraj("kraj");
    std::vector<std::shared_ptr<Pregled>> v;
    Pregledi P;
    while(1) {
        std::cout << "Unesite ime novog pacijenta ili 'kraj' za zavrsetak unosa: ";
        std::getline(std::cin, name);
        if(name == kraj) break;
        std::cout << "Unesite dan mjesec i godinu pregleda: ";
        int dan, mjesec, godina;
        std::cin >> dan >> mjesec >> godina;
        try {
            Datum d(dan,mjesec,godina);
        } catch(std::domain_error e6) {
            std::cout << e6.what() << std::endl;
            return 0;
        }
        std::cout << "Unesite sate i minute pregleda: ";
        int sati, minute;
        std::cin >> sati >> minute;
        try {
            Vrijeme v(sati,minute);
        } catch(std::domain_error e7) {
            std::cout << e7.what() << std::endl;
            return 0;
        }
        v.push_back(std::make_shared<Pregled>(name,Datum(dan,mjesec,godina),Vrijeme(sati,minute)));
        broj_pregleda++;
        std::cin.ignore(10000,'\n');
        try {
            P.RegistrirajPregled(name,dan,mjesec,godina,sati,minute);
        } catch(std::range_error e2) {
            std::cout << e2.what() << std::endl;
            return 0;
        }
    }
    std::cout << "Trenutno su registrovani sljedeci pregledi\n";
    P.IspisiSvePreglede();
    int n(0);
    while(n != 7) {
        std::cout << "Odaberite jednu od sljedecih opcija\n";
        std::cout << "1 - Broj pregleda na datum\n";
        std::cout << "2 - Najraniji pregled\n";
        std::cout << "3 - Obrisi pregled pacijenta\n";
        std::cout << "4 - Obrisi najraniji pregled\n";
        std::cout << "5 - Ispisi sve pregleda na datum\n";
        std::cout << "6 - Ispisi sve preglede\n";
        std::cout << "7 - Kraj programa\n";
        std::cin >> n;
        if(n == 7) break;
        switch(n) {
        case 1: {
            std::cout << "Unesite dan mjesec i godinu : ";
            int dan, mjesec, godina;
            std::cin >> dan >> mjesec >> godina;
            try {
                P.DajBrojPregledaNaDatum(Datum(dan,mjesec,godina));
            } catch(std::domain_error e5) {
                std::cout << e5.what() << std::endl;
                return 0;
            }
            std::cout << "Broj pregleda na datum " << dan << " " << mjesec << " " << godina << " je: ";
            std::cout << P.DajBrojPregledaNaDatum(Datum(dan,mjesec,godina)) << std::endl;
            break;
        }
        case 2: {
            try {
                P.DajNajranijiPregled();
            } catch(std::domain_error e3) {
                std::cout << e3.what() << std::endl;
                return 0;
            }
            std::cout << "Najraniji pregled je:\n";
            P.DajNajranijiPregled().Ispisi();
            std::cout << std::endl;
            break;
        }
        case 3: {
            std::cout << "Unesite ime pacijenta: ";
            std::string ime1;
            std::cin.ignore(1000,'\n');
            std::getline(std::cin,ime1);
            int br_pr(P.DajBrojPregleda());
            P.ObrisiPregledePacijenata(ime1);
            std::cout << "Uspjesno obrisano " << br_pr - P.DajBrojPregleda() << " pregleda\n";
            break;
        }
        case 4: {
            try {
                P.ObrisiNajranijiPregled();
            } catch(std::range_error e4) {
                std::cout << e4.what() << std::endl;
                return 0;
            }
            std::cout << "Najraniji pregled uspjesno obrisan\n";
            break;
        }
        case 5: {
            std::cout << "Unesite dan mjesec i godinu : ";
            int dan, mjesec, godina;
            std::cin >> dan >> mjesec >> godina;
            std::cout << "Pregledi na datum " << dan << " " << mjesec << " " << godina << " su:\n";
            P.IspisiPregledeNaDatum(Datum(dan,mjesec,godina));
            break;
        }
        case 6: {
            P.IspisiSvePreglede();
            break;
        }
        }
    }
    return 0;
}
