.PHONY: help init
.DEFAULT_GOAL = help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


init: ## Install external dependencies to run this project
	curl -LfO https://airflow.apache.org/docs/apache-airflow/3.1.0/docker-compose.yaml
# 	mkdir ./dags ./logs ./plugins
# 	@echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
