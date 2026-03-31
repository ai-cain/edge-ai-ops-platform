#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef _WIN32
#define CURL_BINARY "curl.exe"
#else
#define CURL_BINARY "curl"
#endif

static const char* get_base_url(int argc, char** argv) {
    const char* env_base_url = getenv("EDGE_AI_OPS_BASE_URL");
    if (argc > 1) {
        return argv[1];
    }
    if (env_base_url != NULL && env_base_url[0] != '\0') {
        return env_base_url;
    }
    return "http://localhost:8000/api/v1";
}

static int post_payload(
    const char* api_base_url,
    const char* path,
    const char* file_name,
    const char* payload
) {
    char command[4096];
    FILE* file = fopen(file_name, "wb");
    if (file == NULL) {
        return 1;
    }

    fputs(payload, file);
    fclose(file);

    snprintf(
        command,
        sizeof(command),
        "%s -sS -X POST -H \"Content-Type: application/json\" --data @\"%s\" \"%s%s\"",
        CURL_BINARY,
        file_name,
        api_base_url,
        path
    );

    const int status = system(command);
    remove(file_name);
    return status;
}

int main(int argc, char** argv) {
    const char* api_base_url = get_base_url(argc, argv);

    printf("Sending external C runtime payloads to %s\n", api_base_url);

    if (
        post_payload(
            api_base_url,
            "/ingest/devices",
            "external_c_devices_payload.json",
            "{\"items\":[{\"id\":\"c-camera-01\",\"name\":\"C Camera 01\",\"device_type\":\"c-runtime\",\"status\":\"online\",\"location\":\"External Runtime Lab\",\"last_seen\":\"2026-03-31T02:20:00Z\"}]}"
        ) ||
        post_payload(
            api_base_url,
            "/ingest/telemetry",
            "external_c_telemetry_payload.json",
            "{\"items\":[{\"device_id\":\"c-camera-01\",\"points\":[{\"timestamp\":\"2026-03-31T02:20:00Z\",\"metric\":\"cpu_load\",\"value\":33.1,\"unit\":\"percent\"},{\"timestamp\":\"2026-03-31T02:20:03Z\",\"metric\":\"cycle_time\",\"value\":14.2,\"unit\":\"ms\"}]}]}"
        ) ||
        post_payload(
            api_base_url,
            "/ingest/ai-events",
            "external_c_events_payload.json",
            "{\"items\":[{\"id\":\"c-event-01\",\"device_id\":\"c-camera-01\",\"event_type\":\"detection\",\"label\":\"misalignment\",\"confidence\":0.91,\"severity\":\"high\",\"created_at\":\"2026-03-31T02:20:05Z\"}]}"
        ) ||
        post_payload(
            api_base_url,
            "/ingest/inspections",
            "external_c_inspections_payload.json",
            "{\"items\":[{\"id\":\"c-insp-01\",\"device_id\":\"c-camera-01\",\"job_id\":\"c-batch-01\",\"result\":\"fail\",\"defect_type\":\"misalignment\",\"score\":0.91,\"evidence_uri\":\"file:///evidence/c/frame-01.jpg\",\"created_at\":\"2026-03-31T02:20:06Z\"}]}"
        )
    ) {
        fprintf(stderr, "One or more C external runtime requests failed.\n");
        return 1;
    }

    printf("External C runtime payloads sent successfully.\n");
    return 0;
}
