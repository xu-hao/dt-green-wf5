class: Workflow
cwlVersion: v1.0
id: workflow5
label: workflow5
$namespaces:
  sbg: 'https://www.sevenbridges.com/'
inputs: []
outputs: 
  question1:
    type: string
    outputSource: module2_4_question1/features
  question2:
    type: string
    outputSource: module2_4_question2/features
steps:
  - id: module1
    in: []
    out:
      - id: cohort_id
    run: ./module1.cwl
    'sbg:x': 0
    'sbg:y': 53.5
  - id: module2_4_question1
    in:
      - id: cohort_id
        source: module1/cohort_id
      - id: maximum_p_value
        default: 0.01
    out:
      - id: features
    run: ./module2_4_question1.cwl
    'sbg:x': 288.359375
    'sbg:y': 240
  - id: module2_4_question2
    in:
      - id: cohort_id
        source: module1/cohort_id
      - id: maximum_p_value
        default: 0.01
    out:
      - id: features
    run: ./module2_4_question2.cwl
    'sbg:x': 281.359375
    'sbg:y': -179
requirements: []
