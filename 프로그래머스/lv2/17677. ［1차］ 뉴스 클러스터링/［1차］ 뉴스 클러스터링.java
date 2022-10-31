import java.util.*;
class Solution {
	public static int solution(String str1, String str2) {
		int answer = 0;
		double union = 0; // 합
		double inter = 0; // 교
		HashMap<String, Integer> map1 = new HashMap<>();
		HashMap<String, Integer> map2 = new HashMap<>();
		str1 = str1.toUpperCase();
		str2 = str2.toUpperCase();
		for (int i = 0; i < str1.length() - 1; i++) {
			String s = str1.substring(i, i + 2).replaceAll("[^A-Z]", "");
			if(s.length() < 2)
				continue;
			map1.put(s, map1.getOrDefault(s, 0) + 1);
		}
		for (int i = 0; i < str2.length() - 1; i++) {
			String s = str2.substring(i, i + 2).replaceAll("[^A-Z]", "");
			if(s.length() < 2)
				continue;
			map2.put(s, map2.getOrDefault(s, 0) + 1);
		}

		if (map1.size() == 0 && map2.size() == 0)
			return 65536;

		for (String key : map1.keySet()) {
			if (map2.containsKey(key)) {
				inter += Math.min(map1.get(key), map2.get(key));
				union += Math.max(map1.get(key), map2.get(key));
				map2.remove(key);
			} else {
				union += map1.get(key);
			}
		}
		for (String key : map2.keySet()) {
			union += map2.get(key);
		}
		return (int) Math.floor((inter / union) * 65536);
	}
}