#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long cl=0,cu=0;
    string s;
    cin>>s;
    for (char i:s){
        if (isupper(i)){
            cu+=1;
        }else{
            cl+=1;
        }
    }
    if (cu>cl){
        for (auto& c:s){
            c=static_cast<char>(toupper(static_cast<unsigned char>(c)));
        }
        cout<<s<<"\n";
    }else{
        for (auto& c:s){
            c=static_cast<char>(tolower(static_cast<unsigned char>(c)));
        }
        cout<<s<<"\n";
    }
}
