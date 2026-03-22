// Simple Android/Kotlin code example for accessing the API
// This would go in an Android app's MainActivity.kt

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import okhttp3.*
import java.io.IOException

class MainActivity : AppCompatActivity() {

    private lateinit var recyclerView: RecyclerView
    private lateinit var studentAdapter: StudentAdapter
    private val students = mutableListOf<Student>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        recyclerView = findViewById(R.id.recyclerView)
        recyclerView.layoutManager = LinearLayoutManager(this)
        studentAdapter = StudentAdapter(students)
        recyclerView.adapter = studentAdapter

        // Fetch students from Django API
        fetchStudents()
    }

    private fun fetchStudents() {
        val client = OkHttpClient()
        val request = Request.Builder()
            .url("http://YOUR_IP_ADDRESS:8000/api/students/")
            .build()

        client.newCall(request).enqueue(object : Callback {
            override fun onFailure(call: Call, e: IOException) {
                runOnUiThread {
                    // Handle error
                }
            }

            override fun onResponse(call: Call, response: Response) {
                response.body?.string()?.let { jsonString ->
                    val gson = Gson()
                    val responseType = object : TypeToken<ApiResponse>() {}.type
                    val apiResponse = gson.fromJson<ApiResponse>(jsonString, responseType)

                    runOnUiThread {
                        students.clear()
                        students.addAll(apiResponse.students)
                        studentAdapter.notifyDataSetChanged()
                    }
                }
            }
        })
    }
}

// Data classes
data class Student(
    val id: Int,
    val enrollment_number: String,
    val first_name: String,
    val last_name: String,
    val email: String,
    val phone: String,
    val city: String,
    val is_active: Boolean
)

data class ApiResponse(
    val success: Boolean,
    val count: Int,
    val students: List<Student>
)