# run scripts in setup/ to install the necessary packages
install_kind:
	@./setup/kind.sh

install_helm:
	@./setup/helm.sh

install:
	install_kind install_helm
