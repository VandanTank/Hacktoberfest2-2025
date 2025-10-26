class Solution {
public:
    string countAndSay(int n) {
        string sequence = "1";
        
        for (int i = 2; i <= n; i++) {
            string temp = "";
            int count = 1;
            
            for (int j = 0; j < sequence.size(); j++) {
                if (j + 1 < sequence.size() && sequence[j] == sequence[j + 1]) {
                    count++;
                } else {
                    temp += to_string(count) + sequence[j];
                    count = 1;
                }
            }
            
            sequence = temp;
        }
        
        return sequence;
    }
};
