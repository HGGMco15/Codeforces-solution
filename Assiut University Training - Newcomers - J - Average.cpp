#include <bits/stdc++.h>
using namespace std;
void solve(){
    vector<long double> a(10000);
    long long n; long double sm=0.0;
    cin>>n;
    for (long long i=0;i<n;++i){
        cin>>a[i];
        sm+=a[i];
    }
    cout<<fixed<<setprecision(7)<<(long double)(sm/n)<<"\n";
}
int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}
