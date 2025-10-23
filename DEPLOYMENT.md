# Deployment Guide - Streamlit Cloud

## IMPORTANT: Python Version Configuration

Streamlit Cloud **DOES NOT** support `runtime.txt` or `.python-version` files for specifying Python versions. These files are ignored.

### How to Set Python Version (REQUIRED)

This app requires **Python 3.11** because MediaPipe does not support Python 3.13.

**Steps:**

1. Go to https://share.streamlit.io/
2. Find your app in the dashboard
3. Click the **3 dots menu (⋮)** → **Settings**
4. Under **Advanced settings**, find **Python version**
5. Select **Python 3.11** from the dropdown
6. Click **Save**
7. The app will automatically redeploy with Python 3.11

### Why Python 3.11?

- MediaPipe (our face detection library) supports Python 3.9, 3.10, 3.11, and 3.12
- MediaPipe **does NOT support Python 3.13** yet
- Streamlit Cloud defaults to Python 3.13 if not configured
- This causes the error: "No matching distribution found for mediapipe"

## Dependencies

All dependencies are in `requirements.txt`:
- streamlit
- mediapipe (requires Python ≤ 3.12)
- opencv-python-headless
- numpy
- pillow
- requests

## Troubleshooting

### Error: "No matching distribution found for mediapipe"
**Cause:** Python 3.13 is being used
**Solution:** Change Python version to 3.11 in Streamlit Cloud settings (see above)

### Error: "mediapipe has no wheels with a matching Python ABI tag"
**Cause:** Same as above
**Solution:** Same as above

## References

- [Streamlit Cloud Python Version Documentation](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/upgrade-python)
- [Community Discussion on Python 3.13 Issue](https://discuss.streamlit.io/t/streamlit-cloud-using-python-3-13-despite-runtime-txt-specifying-3-11/113759)
