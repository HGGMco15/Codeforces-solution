#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long t,n,val;
    cin>>t;
    for (long long i=0;i<t;++i){
        vector<long long> a;
        cin>>n;
        for (long long j=0;j<n;++j){
            cin>>val;
            a.push_back(val);
        }
        long long ct1=count(a.begin(),a.end(),1);
        long long ct0=count(a.begin(),a.end(),0);
        if (ct1>=ct0){
            cout<<"Bessie"<<"\n";
        }else{
            cout<<"Elsie"<<"\n";
        }
    }   
}
