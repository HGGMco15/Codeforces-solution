#include <iostream>
#include <algorithm>
#include <cctype>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    string s,st="";
    cin>>s;
    for (char i:s){
        char d=tolower(i);
        if (d!='a' && d!='i' && d!='u' && d!='e' && d!='o' && d!='y'){
            if (isupper(i)){
                cout<<"."<<(char)tolower(i);
            }else{
                cout<<"."<<(char)tolower(i);
            }
        }
    }
}
