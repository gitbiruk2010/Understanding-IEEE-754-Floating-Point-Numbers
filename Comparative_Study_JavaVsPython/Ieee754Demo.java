import java.math.BigDecimal;
import java.math.MathContext;
import java.math.RoundingMode;

public class Ieee754Demo {

    public static void demonstrateIeee754Java() {
        // Setting up the math context
        MathContext mc = new MathContext(34, RoundingMode.HALF_EVEN);

        // Demo rounding
        BigDecimal value = new BigDecimal("1.2345678901234567890123456789012345");
        BigDecimal roundedValue = value.round(mc);
        System.out.println("Rounded value in Java: " + roundedValue);

        // Demo overflow
        try {
            BigDecimal result = new BigDecimal("1e1000").multiply(new BigDecimal("1e1000"));
            System.out.println(result);  // This line will not be executed if overflow occurs
        } catch (ArithmeticException e) {
            System.out.println("Overflow occurred in Java");
        }

        // Demo underflow
        try {
            BigDecimal result = new BigDecimal("1e-1000").multiply(new BigDecimal("1e-1000"));
            System.out.println(result);  // This line will not be executed if underflow occurs
        } catch (ArithmeticException e) {
            System.out.println("Underflow occurred in Java");
        }

        // Demo invalid operation
        try {
            BigDecimal result = new BigDecimal("0").divide(new BigDecimal("0"));
            System.out.println(result);  // This line will not be executed if invalid operation occurs
        } catch (ArithmeticException e) {
            System.out.println("Invalid operation in Java");
        }
    }

    public static void main(String[] args) {
        demonstrateIeee754Java();
    }
}
