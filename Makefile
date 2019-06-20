plugindir=extensions/stealth_bot

all: ${plugindir}/*
	$(MAKE) -C $(plugindir)
		
