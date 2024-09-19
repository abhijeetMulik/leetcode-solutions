class Solution {
    public int firstUniqChar(String s) {
         // Use a HashMap to store the indices of each character
        Map<Character, List<Integer>> seen = new LinkedHashMap<>();
        
        // Iterate over the string and store indices for each character
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            // If the character is not yet in the map, create a new list for it
            seen.putIfAbsent(c, new ArrayList<>());
            // Add the current index to the character's list of indices
            seen.get(c).add(i);
        }

        for(List<Integer> indices : seen.values()){
            if(indices.size() == 1){
                return indices.get(0);
            }
        }

        
        return -1;
    }
}