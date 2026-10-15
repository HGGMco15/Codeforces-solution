#include <bits/stdc++.h>
using namespace std;
void solve(){
    long long t,n;
    char s;
    cin>>t;
    for (long long i=0;i<t;++i){
        cin>>n>>s;
        for (long long j=0;j<n;++j){
            cout<<s<<" ";
        }
        cout<<"\n";
    }
}
int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}
