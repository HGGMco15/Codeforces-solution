#include <bits/stdc++.h>
using namespace std;
 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long t,n;
    cin>>t;
    for (long long i=0;i<t;++i){
        long long mx=-1e12,mn=1e12;
        cin>>n;
        vector<long long> a(n);
        for (long long j=0;j<n;++j){
            cin>>a[j];
            mx=max(mx,a[j]);
            mn=min(mn,a[j]);
        }
        cout<<((mx+1)-mn)<<"\n";
    }
    return 0;
}
