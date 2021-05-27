#include <iostream>
#include <vector>

using namespace std;


// Create getPos namspace
namespace getPos
{
    /**
     * Find the position of a string
     * in a vector of strings
     */
    pair<int, int> findPosition(vector <string>& vec, string& str, int m)
    {
        // Position is an int pair
        pair<int, int> position;

        // Iterate over each row
        for (int row = 0; row < m; row++)
        {
            // Iterate over each column in the row
            size_t column = vec[row].find(str);

            // 'm' or 'p' are found
            if (column != string::npos)
            {
                position.first = row;
                position.second = column;
            }
        }

    return position;
    }
};


/**
 * Displays the moves 'm' must take to
 * rescue 'p', one move per line.
 */
void displayPathtoPrincess(int m, vector <string> grid)
{
    // Strings to be found
    string mario = "m";
    string princess = "p";

    // Position of strings
    pair<int, int> pos_m = getPos::findPosition(grid, mario, m);        // Use getPos namespace
    pair<int, int> pos_p = getPos::findPosition(grid, princess, m);

    // Distance between strings
    int row_dif = pos_m.second - pos_p.second;
    int col_dif = pos_m.first - pos_p.first;

    // While Princess not saved output move
    while (row_dif != 0 || col_dif != 0)
    {
        if (row_dif > 0)
        {
            cout << "LEFT" << "\n";
            row_dif -= 1;
        }
        else if (row_dif < 0)
        {
            cout << "RIGHT" << "\n";
            row_dif += 1;
        }
        else if (col_dif > 0)
        {
            cout << "UP" << "\n";
            col_dif -= 1;
        }
        else
        {
            cout << "DOWN" << "\n";
            col_dif += 1;
        }
    }
}


// HackerRank main function
int main(void)
{
    int m;                  // Size of grid
    vector <string> grid;   // Grid is a vector of strings

    cin >> m;   // Input size

    // Input m strings of size m
    for(int i = 0; i < m; i++)
    {
        string s; cin >> s;
        grid.push_back(s);
    }

    displayPathtoPrincess(m, grid);

    return 0;
}
