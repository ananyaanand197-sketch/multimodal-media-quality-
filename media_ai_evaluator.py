import json
import random

def evaluate_ai_media(file_name, media_type="image"):
    print(f"--- Evaluating Multimodal Asset: {file_name} ---")
    
    # Simulate automated computer vision metric scoring
    blur_score = round(random.uniform(0.1, 0.95), 2)
    artifact_detected = random.choice([True, False])
    anatomical_consistency = round(random.uniform(0.70, 0.99), 2)
    
    passed_qa = (blur_score > 0.50) and (not artifact_detected) and (anatomical_consistency > 0.80)
    
    report = {
        "asset_name": file_name,
        "type": media_type,
        "metrics": {
            "clarity_score": blur_score,
            "artifact_detected": artifact_detected,
            "anatomy_score": anatomical_consistency
        },
        "status": "APPROVED" if passed_qa else "REJECTED_NEEDS_REVIEW"
    }
    
    print(json.dumps(report, indent=2))
    return report

if __name__ == "__main__":
    evaluate_ai_media("generated_person_portrait_01.png", "image")
    evaluate_ai_media("ai_video_clip_sample.mp4", "video")