import java.io.File;
import java.util.*;

public class file {
    public static void main(String[] args){

        System.out.println("Enter File name:");
        Scanner i = new Scanner(System.in);
        String fname = i.next();
        File f1 = new File(fname);
        System.out.println("Filename : "+ f1.getName());
        f1.setWritable(true);

        System.out.println(f1.exists()?"File Exists ":"File does not Exists ");
        System.out.println(f1.canWrite()?"File write ":"File is not writable ");
        System.out.println(f1.canRead()?"File Readable ":"File is not Readable ");

        String filename = f1.toString();
        int index = filename.indexOf('.');
        if (index>0)
        {
            String type = filename.substring(index+1);
            System.out.println("File type id "+ type);
        }
        else{
            System.out.println("File doesnt have a  type");
        }
    }
}
