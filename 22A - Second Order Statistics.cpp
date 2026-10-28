#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n,mn=1e9;
    cin>>n;
    vector<long long> a(n);
    for (long long i=0;i<n;++i){
        cin>>a[i];
        mn=min(mn,a[i]);
    }
    set<long long> b(a.begin(),a.end());
    if (b.size()==1){
        cout<<"NO"<<"\n";
    }else{
        for (long long i:b){
            if (i>mn){
                cout<<i<<"\n";
                break;
            }
        }
    }
}
