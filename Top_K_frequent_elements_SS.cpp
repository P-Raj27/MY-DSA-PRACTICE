//using priority queue

//top k frequent elements
#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> v={6,1,1,1,2,2,3};
    int k=2;
    map<int,int> m;

    vector<int> result;
    int num;

    priority_queue<pair<int,int>> pair1;

    for(int i=0;i<v.size();i++)
    m[v[i]]++;

    for(auto i:m)
        pair1.push(make_pair(i.second,i.first));


  


    for(int i=0;i<k;i++) 
    {

        result.push_back(pair1.top().second);
    
        pair1.pop();
    } 


    for(int i=0;i<k;i++)
    cout<<result[i]<<" ";



    




}
