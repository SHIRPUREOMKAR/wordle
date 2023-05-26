#include<iostream>
#include<fstream>
#include<cstring>
#include<chrono>

using namespace std;
using namespace std::chrono;

int main(){
    auto start = high_resolution_clock::now();
    string str;
    string line;
    bool success = true;

    fstream rfile;
    rfile.open("output.txt", ios::in);
    fstream file;
    file.open("temp.txt", ios::out);
    if(rfile.is_open()){
        getline(rfile, line);
        for(int i = 0; i <line.length(); i++){
            if(line[i] == ' '){
                file << "\n";
            }
            else{
                file << line[i];
            }
        }
        file.close();
        rfile.close();
    }

    // if(rfile.is_open()){
    //     getline(rfile, line);
    //     int counter = 0;
    //     while(counter < line.length()){
    //         string t = "";
    //         for(int i = 0; i < 13; i++){
    //             t += line[counter];
    //             counter++;
    //         }
    //         file << t << "\n";
    //         counter += 2;
    //     }

    //     file.close();
    //     rfile.close();      
    // }

    fstream something;
    something.open("temp.txt", ios::in);
    fstream final;
    final.open("13_without_rep.txt", ios::out);

    if(something.is_open()){
        while(!something.eof()){
            getline(something, str);

            success = true;
            for(int i = 0; i < str.length(); i++){
                for(int j = i+1; j < str.length(); j++){
                    if(str[i] == str[j]){
                        success = false;
                    }
                }
            }
            if(success == true){
                final << str <<"\n";
            }
        }

        final.close();
        something.close();
    }
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    cout <<"Execution time : "<< duration.count() <<" microseconds"<< endl;
}