#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<long long> a={4,7,44,47,74,77,444,447,477,474,777,774,744,747};
    long long n; bool flag=false;
    cin>>n;
    for (long long i:a){
        if (n%i==0){
            flag=true;
        }
    }
    if (flag){cout<<"YES"<<"\n";}
    else {cout<<"NO"<<"\n";}
}
