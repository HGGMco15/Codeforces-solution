#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n;
    string s,t;
    cin>>n;
    for (long long i=0;i<n;++i){
        cin>>s>>t;
        string st="";
        if (s.size()==t.size()){
            for (long long x=0;x<s.size();++x){
                st+=s[x];
                st+=t[x];
            }
            cout<<st<<"\n";
        }else if (s.size()>t.size()){
            for (long long x=0;x<t.size();++x){
                st+=s[x];
                st+=t[x];
            }
            for (long long x=t.size();x<s.size();++x){
                st+=s[x];
            }
            cout<<st<<"\n";
        }else{
            for (long long x=0;x<s.size();++x){
                st+=s[x];
                st+=t[x];
            }
            for (long long x=s.size();x<t.size();++x){
                st+=t[x];
            }
            cout<<st<<"\n";
        }
    }
}
