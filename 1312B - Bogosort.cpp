#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long t,n;
    cin>>t;
    for (long long i=0;i<t;++i){
        cin>>n;
        vector<long long> a(n);
        for (long long j=0;j<n;++j){cin>>a[j];}
        sort(a.begin(),a.end(),greater<long long>());
        for (long long j:a){
            cout<<j<<" ";
        }
        cout<<"\n";
    }
}
