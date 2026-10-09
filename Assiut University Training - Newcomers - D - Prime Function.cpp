#include <bits/stdc++.h>
using namespace std;
bool prime(long long& m){
    if (m<2){
        return false;
    }if (m<=3){
        return true;
    }if (m%2==0 || m%3==0){
        return false;
    }
    long long i=5;
    while (i*i<=m){
        if (m%i==0 || m%(i+2)==0){
            return false;
        }
        i+=6;
    }
    return true;
}
int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long t,n;
    cin>>t;
    for (long long j=0;j<t;++j){
        cin>>n;
        if (prime(n)){
            cout<<"YES"<<"\n";
        }else{
            cout<<"NO"<<"\n";
        }
    }
}
