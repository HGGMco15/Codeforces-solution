#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long a,b,q;
    cin>>a>>b>>q;
    if (q%3==1){cout<<a<<"\n";}
    else if (q%3==2){cout<<b<<"\n";}
    else{cout<<(a^b)<<"\n";}
    return 0;
}
