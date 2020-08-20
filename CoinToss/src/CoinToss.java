import java.util.Random;

public class CoinToss {

    private String side_up;

    public void toss(){
        Random random = new Random();
        int randomNumber;

        randomNumber = random.nextInt(2);
        if(randomNumber == 0) {
            side_up = "Tails";
        } else {
            side_up = "Heads";
        }
    }

    public String getSide_up(){
        return side_up;
    }

    public CoinToss() {
        toss();
    }
}

