#cool part https://gist.github.com/vratiu/9780109i
RED='\033[0;31m'
Cyan='\033[0;36m'
Green='\033[0;32m'
Yellow='\033[0;33m'
NC='\033[0m' # No Color
ROOT=$PWD

printf "${Yellow}Setup bert model PATH...\n"
export PATHNAME="${ROOT}/model/chinese_L-12_H-768_A-12"
printf "${Cyan}done!!!\n"

printf "${Yellow}Setup python venv environment...\n"
source ${HOME}/bert-Agus/venv/bin/activate
printf "${Cyan}done!!!\n"
printf "${Yellow}Great!!! ${Cyan} Now, everyone is happy! ${RED}(◕ ‿ ◕ )!${NC}\n"

printf "${Yellow}Starting bert as a service...\n"
bert-serving-start -model_dir ${PATHNAME} -num_worker=1
