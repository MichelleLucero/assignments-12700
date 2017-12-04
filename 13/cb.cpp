#include <iostream>
#include <string>

using namespace std;

int cigar_party(int c,bool weekend){
    if(!weekend && 40 <= c && c <= 60){
        return true;
    }

    if(weekend && 40 <= c){
        return true;
    }

    else{
        return false;
    }

}


int lone_sum(int a,int b, int c){

    if(a == b == c){
        return 0;
    }

    if(a == b){
        return c;
    }

    if(b == c){
        return a;
    }

    if(c == a){
        return b;
    }

    else{
        return a + b + c;
    }





}



int main(){

    bool party = cigar_party(20, false);
    bool party_one = cigar_party(70, true);
    cout << "Cigar Party" << endl;
    cout << "(20 cigars, weekday) " << boolalpha << party << endl;
    cout << "(70 cigars, weekend) " << boolalpha <<party_one << endl;

    cout << "lone sum" << endl;
    cout << "lone sum result of 3,3,4 is " << lone_sum(3,3,4) <<endl;
    cout << "lone sum result of 3,2,4 is " << lone_sum(3,2,4) <<endl;
    cout << "lone sum result of 3,3,3 is " << lone_sum(3,3,3) <<endl;
    return 0;
}  