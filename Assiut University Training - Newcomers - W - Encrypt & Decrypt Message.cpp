#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long q;
    string s,key="PgEfTYaWGHjDAmxQqFLRpCJBownyUKZXkbvzIdshurMilNSVOtec#@_!=.+-*/",org="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    cin>>q;
    cin>>s;
    if (q==1){
        string st="";
        for (const char& i:s){
            auto it=find(org.begin(),org.end(),i);
            long long d=distance(org.begin(),it);
            st+=key[d];
        }
        cout<<st<<"\n";
    }else{
        string st="";
        for (const char& i:s){
            auto it=find(key.begin(),key.end(),i);
            long long d=distance(key.begin(),it);
            st+=org[d];
        }
        cout<<st<<"\n";
    }
}
