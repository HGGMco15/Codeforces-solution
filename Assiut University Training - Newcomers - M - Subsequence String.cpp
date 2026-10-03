#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    string s,tar="hello";
    long long cur=0,ct=0;
    cin>>s;
    for (const char& i:s){
        if (i==tar[cur]){
            ct+=1;
            cur+=1;
        }
        if (ct==5){
            break;
        }
    }
    if (ct==5){
        cout<<"YES"<<"\n";
    }else{
        cout<<"NO"<<"\n";
    }
}
