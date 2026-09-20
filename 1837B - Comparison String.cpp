#include <bits/stdc++.h>
using namespace std;
void solve(const string& s){
    long long c1=1,cur=1;
    for (long long i=1;i<s.size();++i){
        if (s[i]==s[i-1]){
            cur+=1;
        }else{
            c1=max(cur,c1);
            cur=1;
        }
    }
    c1=max(cur,c1);
    cout<<(c1+1)<<"\n";
}
int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long t,n;
    cin>>t;
    string d;
    for (long long x=0;x<t;++x){
        cin>>n;
        cin>>d;
        solve(d);
    }
}
