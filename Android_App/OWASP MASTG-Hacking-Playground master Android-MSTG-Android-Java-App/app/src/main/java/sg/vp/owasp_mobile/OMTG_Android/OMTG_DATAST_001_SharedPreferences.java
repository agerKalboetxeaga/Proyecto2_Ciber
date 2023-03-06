package sg.vp.owasp_mobile.OMTG_Android;

import android.content.SharedPreferences;
import android.os.Build;
import android.os.Bundle;
import android.security.keystore.KeyGenParameterSpec;
import android.security.keystore.KeyProperties;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.RequiresApi;
import androidx.security.crypto.EncryptedSharedPreferences;
import androidx.security.crypto.MasterKey;
import static android.content.Context.MODE_WORLD_READABLE;

public class OMTG_DATAST_001_SharedPreferences extends AppCompatActivity {

    private Toast toast;
    static final int KEY_SIZE = MasterKey.DEFAULT_AES_GCM_MASTER_KEY_SIZE;
    static final String MASTER_KEY_ALIAS = MasterKey.DEFAULT_MASTER_KEY_ALIAS;
    private MasterKey masterKey;

    @RequiresApi(api = Build.VERSION_CODES.M)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_omtg__datast_001__shared_preference);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        try {
            gakoakSortu();
            enkriptatu();
        }
        catch(Exception e) {
            Toast.makeText(this, "Exception " + e.getMessage() + " occured", Toast.LENGTH_LONG).show();
        }

        //SharedPreferences sharedPref = getSharedPreferences("key", MODE_PRIVATE);
        //SharedPreferences.Editor editor = sharedPref.edit();
        //editor.putString("username", "administrator");
        //editor.putString("password", "supersecret");
        //editor.commit();

    }


    @android.support.annotation.RequiresApi(api = Build.VERSION_CODES.M)
    public void gakoakSortu() {
        try {
            KeyGenParameterSpec spec = new KeyGenParameterSpec.Builder(
                    MASTER_KEY_ALIAS,
                    KeyProperties.PURPOSE_ENCRYPT | KeyProperties.PURPOSE_DECRYPT)
                    .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
                    .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
                    .setKeySize(KEY_SIZE)
                    .build();

            masterKey = new MasterKey.Builder(this)
                    .setKeyGenParameterSpec(spec)
                    .build();
        } catch (Exception e) {
            Toast.makeText(this, "Exception " + e.getMessage() + " occured", Toast.LENGTH_LONG).show();
        }
    }

    @android.support.annotation.RequiresApi(api = Build.VERSION_CODES.M)
    public void enkriptatu() {
        try {
            SharedPreferences sharedPreferences = EncryptedSharedPreferences.create(this, "key",
                    masterKey,
                    EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
                    EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
            );
            // storing a value
            sharedPreferences.edit().putString("username", "izaskun").putString("password", "password").apply();
            // reading a value
            TextView helloTextView = (TextView) findViewById(R.id.title);
            helloTextView.setText(sharedPreferences.getString("username",""));
        }
        catch(Exception e) {
            Toast.makeText(this, "Exception " + e.getMessage() + " occured", Toast.LENGTH_LONG).show();
        }
    }


}
