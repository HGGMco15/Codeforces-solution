#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long a,b,t,mx,mn;
    cin>>t;
    for (long long i=0;i<t;++i){
        cin>>a>>b;
        if (a==b){
            cout<<"0 0"<<"\n";
        }else{
            mx=abs(a-b);
            cout<<mx<<" "<<min(a%mx,mx-(a%mx))<<"\n";
        }
    }
}
