#include <bits/stdc++.h>
using namespace std;
bool palindrome(string& s){
    string ne=s;
    reverse(ne.begin(),ne.end());
    return ne==s;
}
int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    string bir="";
    long long n,org;
    cin>>n; org=n;
    while (n>0){
        bir+=to_string(n%2);
        n/=2;
    }
    if (org%2!=0 && palindrome(bir)){
        cout<<"YES"<<"\n";
    }else{
        cout<<"NO"<<"\n";
    }
}
