#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n,val,val2;
    vector<long long> a,b;
    cin>>n;
    for (long long i=0;i<n;++i){
        cin>>val>>val2;
        a.push_back(val);
        b.push_back(val2);
    }
    bool shit=false;
    for (long long x=0;x<a.size();++x){
        auto sh=find(a.begin(),a.end(),a[x]+b[x]);
        if (sh!=a.end()){
            long long f=distance(a.begin(),sh);
            if (a[f]+b[f]==a[x]){
                shit=true;
                break;
            }
        }
    }
    if (shit){
        cout<<"YES"<<"\n";
    }else{
        cout<<"NO"<<"\n";
    }
}
