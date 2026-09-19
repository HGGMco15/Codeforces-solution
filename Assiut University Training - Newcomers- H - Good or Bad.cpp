#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long t;
    string s;
    cin>>t;
    for (long long i=0;i<t;++i){
        bool sh=false;
        cin>>s;
        for (long long j=0;j<s.size()-2;++j){
            string sub=s.substr(j,3);
            if (sub=="010" || sub=="101"){
                sh=true;
            }
        }
        if (sh){
        cout<<"Good"<<"\n";
        }else{
            cout<<"Bad"<<"\n";
        }
    }
}
