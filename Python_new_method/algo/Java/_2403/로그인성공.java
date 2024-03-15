public class 로그인성공 {
    public static void main(String[] args) {
        String[] id_pw = {"meosseugi", "1234"};
        String[][] db = {{"rardss", "123"}, {"yyoom", "1234"}, {"meosseugi", "1234"}};
        X.s(id_pw,db);

    }

    private static class X {
        public static String s(String[] id_pw, String[][] db) {
            for (int i=0; i < db.length; i++) {
                if (db[i][0].equals(id_pw[0])&& db[i][1].equals(id_pw[1])) return "login";
                else if (db[i][0].equals(id_pw[0])) return "wrong pw";
            }
            return "fail";
        }
    }
}


