#include <bits/stdc++.h>
using namespace std;
long long solve(long long a,long long b){
    long long ans=0,val=a;
    for (long long i=2;i<=b;i+=2){
        for (long long j=1;j<i;++j){
            val*=a;
        }
        ans+=val;
        val=a;
    }
    return ans;
}
int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long x,n;
    cin>>x>>n;
    cout<<solve(x,n)<<"\n";
}
