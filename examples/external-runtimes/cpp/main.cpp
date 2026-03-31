#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>

namespace {

std::string base_url(int argc, char** argv) {
    if (argc > 1) {
        return argv[1];
    }

    if (const char* env = std::getenv("EDGE_AI_OPS_BASE_URL")) {
        return env;
    }

    return "http://localhost:8000/api/v1";
}

std::string curl_binary() {
#ifdef _WIN32
    return "curl.exe";
#else
    return "curl";
#endif
}

std::filesystem::path write_payload(const std::string& stem, const std::string& payload) {
    const auto file_path = std::filesystem::temp_directory_path() / (stem + ".json");
    std::ofstream output(file_path, std::ios::binary);
    output << payload;
    output.close();
    return file_path;
}

int post_payload(
    const std::string& api_base_url,
    const std::string& path,
    const std::string& stem,
    const std::string& payload
) {
    const auto payload_path = write_payload(stem, payload);
    const std::string command =
        curl_binary() +
        " -sS -X POST -H \"Content-Type: application/json\" --data @" +
        "\"" + payload_path.string() + "\" \"" + api_base_url + path + "\"";
    const int exit_code = std::system(command.c_str());
    std::filesystem::remove(payload_path);
    return exit_code;
}

} // namespace

int main(int argc, char** argv) {
    const std::string api_base = base_url(argc, argv);

    std::cout << "Sending external C++ runtime payloads to " << api_base << '\n';

    const int devices_status = post_payload(
        api_base,
        "/ingest/devices",
        "edge-ai-ops-cpp-devices",
        R"({"items":[{"id":"cpp-camera-01","name":"C++ Camera 01","device_type":"cpp-runtime","status":"online","location":"External Runtime Lab","last_seen":"2026-03-31T02:10:00Z"}]})"
    );
    const int telemetry_status = post_payload(
        api_base,
        "/ingest/telemetry",
        "edge-ai-ops-cpp-telemetry",
        R"({"items":[{"device_id":"cpp-camera-01","points":[{"timestamp":"2026-03-31T02:10:00Z","metric":"gpu_temp","value":58.4,"unit":"celsius"},{"timestamp":"2026-03-31T02:10:03Z","metric":"fps","value":29.7,"unit":"fps"}]}]})"
    );
    const int events_status = post_payload(
        api_base,
        "/ingest/ai-events",
        "edge-ai-ops-cpp-events",
        R"({"items":[{"id":"cpp-event-01","device_id":"cpp-camera-01","event_type":"anomaly","label":"surface_scratch","confidence":0.94,"severity":"high","created_at":"2026-03-31T02:10:05Z"}]})"
    );
    const int inspections_status = post_payload(
        api_base,
        "/ingest/inspections",
        "edge-ai-ops-cpp-inspections",
        R"({"items":[{"id":"cpp-insp-01","device_id":"cpp-camera-01","job_id":"cpp-batch-01","result":"fail","defect_type":"surface_scratch","score":0.94,"evidence_uri":"file:///evidence/cpp/frame-01.jpg","created_at":"2026-03-31T02:10:06Z"}]})"
    );

    if (devices_status || telemetry_status || events_status || inspections_status) {
        std::cerr << "One or more C++ external runtime requests failed.\n";
        return 1;
    }

    std::cout << "External C++ runtime payloads sent successfully.\n";
    return 0;
}
