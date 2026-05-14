# Plan

> [!note]
> This plan was created by Gemini, it can be wrong or right, remember to review it first before implementing

## Step 1: Implementing Airflow DAG Logic

**Context:** Edit the file `starter_project/dags/sales_data_quality_pipeline.py`.
Task: Replace the `validate_orders_task` function's `NotImplementedError` with the actual implementation.

**Requirements:**

1. Import `AIRFLOW_INPUT_FILE` and `SUMMARY_FILE` from `src.config`.

2. Import `run_lab_check` from `src.validation`.

3. Inside the function, call `run_lab_check()`.

4. Pass `AIRFLOW_INPUT_FILE` as the `input_path`.

5. Pass `SUMMARY_FILE` as the output_path.

6. Set `allow_failure=False` so the Airflow task explicitly fails if the validation fails.

7. Set `skip_discord=False` so alerts are sent.

8. Return the summary dictionary.

## Step 2: Set Up Environment Variables

**Context:** Read `starter_project/.env.example`.

**Task:** Create a new file named `starter_project/.env`.

**Requirements:** Copy the contents of the `.env.example` file into the new `.env` file. Leave `DISCORD_WEBHOOK_URL` as a placeholder, but add a comment reminding the user to replace it with a real Discord webhook URL before running the Airflow pipeline.

## Step 3: Run Local Verification Tests

**Context:** The code is now implemented.

**Task:** Execute the local testing scripts to verify the implementation.

**Commands to run:**

`uv run python starter_project/scripts/run_local_check.py starter_project/data/orders_passed.csv --skip-discord`

`uv run python3 starter_project/scripts/run_local_check.py starter_project/data/orders_failed.csv --allow-failure --skip-discord`

**Requirements:** Read the console output and verify that the first command outputs a summary with `"validation_status": "passed"` and the second command outputs `"validation_status": "failed"`. Output a brief confirmation that the tests passed.
