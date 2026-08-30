#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n,val,sm=0,sm2=0;
    vector<long long> a;
    cin>>n;
    for (int i=0;i<n;++i){
        cin>>val;
        sm+=val;
        a.push_back(val);
    }
    long long org=sm;
    sort(a.begin(),a.end(),greater<>());
    for (int i=0;i<n;++i){
        sm2+=a[i];
        sm=org-sm2;
        if (sm2>sm){
            cout<<(i+1)<<"\n";
            break;
        }
    }
} // First problem using C++
