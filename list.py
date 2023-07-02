import log

def print_general_list():
    print(f'{log.default}General Cyphers{log.reset}')
    print(f'{log.default}1.) {log.reset}List all kerberoastable users')
    print(f'{log.default}2.) {log.reset}List user CanRDP privileges')
    print(f'{log.default}3.) {log.reset}List group CanRDP privileges')
    print(f'{log.default}4.) {log.reset}List all Unconstrained Delegation')
    print(f'{log.default}5.) {log.reset}List all unsupported OSs')
    print(f'{log.default}6.) {log.reset}List groups containing "admin"')
    print(f'{log.default}7.) {log.reset}List users containing "admin"')
    print(f'{log.default}8.) {log.reset}List all user shortest paths to admin groups')
    print(f'{log.default}9.) {log.reset}List all group shortest paths to admin groups')
    print(f'{log.default}10.) {log.reset}List all computer shortest paths to admin groups')
    print(f'{log.default}11.) {log.reset}List groups containing "sql"')
    print(f'{log.default}12.) {log.reset}List users containing "sql"')
    print(f'{log.default}13.) {log.reset}List computers containing "sql"')
    print(f'{log.default}14.) {log.reset}List all user shortest paths to SQL groups')
    print(f'{log.default}15.) {log.reset}List all group shortest paths to SQL groups')
    print(f'{log.default}16.) {log.reset}List all computer shortest paths to SQL groups')
    print(f'{log.default}17.) {log.reset}List users containing "svc/service"')
    print(f'{log.default}18.) {log.reset}List all user shortest paths to service groups')
    print(f'{log.default}19.) {log.reset}List all group shortest paths to service groups')
    print(f'{log.default}20.) {log.reset}List all computer shortest paths to service groups')
    print(f'{log.default}21.) {log.reset}List users containing "web"')
    print(f'{log.default}22.) {log.reset}List groups containing "web"')
    print(f'{log.default}23.) {log.reset}List computers containing "web"')
    print(f'{log.default}24.) {log.reset}List all user shortest paths to web groups')
    print(f'{log.default}25.) {log.reset}List all group shortest paths to web groups')
    print(f'{log.default}26.) {log.reset}List all computer shortest paths to web groups')
    print(f'{log.default}27.) {log.reset}List users containing "dev"')
    print(f'{log.default}28.) {log.reset}List groups containing "dev"')
    print(f'{log.default}29.) {log.reset}List computers containing "dev"')
    print(f'{log.default}30.) {log.reset}List users containing "prod"')
    print(f'{log.default}31.) {log.reset}List groups containing "prod"')
    print(f'{log.default}32.) {log.reset}List computers containing "prod"')
    print(f'{log.default}33.) {log.reset}List all Domain Admins')
    print(f'{log.default}34.) {log.reset}List all user shortest paths to Domain Admins')
    print(f'{log.default}35.) {log.reset}List all group shortest paths to Domain Admins')
    print(f'{log.default}36.) {log.reset}List all computer shortest paths to Domain Admins')
    print(f'{log.default}37.) {log.reset}List all Enterprise Admins')
    print(f'{log.default}38.) {log.reset}List all user shortest paths to Enterprise Admins')
    print(f'{log.default}39.) {log.reset}List all group shortest paths to Enterprise Admins')
    print(f'{log.default}40.) {log.reset}List all computer shortest paths to Enterprise Admins')
    print(f'{log.default}41.) {log.reset}List all sessions')
    print(f'{log.default}42.) {log.reset}List all AS-REP roastable users')
    print(f'{log.default}43.) {log.reset}List all high-value groups')
    print(f'{log.default}44.) {log.reset}List all members of high-value grDowntimeoups')
    print(f'{log.default}45.) {log.reset}List all user shortest paths to high-value targets')
    print(f'{log.default}46.) {log.reset}List all group shortest paths to high-value targets')
    print(f'{log.default}47.) {log.reset}List all computer shortest paths to high-value targets')
    print(f'{log.default}48.) {log.reset}List all user shortest paths to Exchange groups')
    print(f'{log.default}49.) {log.reset}List all group shortest paths to Exchange groups')
    print(f'{log.default}50.) {log.reset}List all computer shortest paths to Exchange groups')
    print(f'{log.default}51.) {log.reset}List user AdminTo privileges')
    print(f'{log.default}52.) {log.reset}List group AdminTo privileges')
    print(f'{log.default}53.) {log.reset}List computer AdminTo privileges')
    print(f'{log.default}54.) {log.reset}List user ReadLAPSPassword privileges')
    print(f'{log.default}55.) {log.reset}List group ReadLAPSPassword privileges')
    print(f'{log.default}56.) {log.reset}List computer ReadLAPSPassword privileges') 
    print(f'{log.default}57.) {log.reset}List user SyncLAPSPassword privileges')
    print(f'{log.default}58.) {log.reset}List group SyncLAPSPassword privileges')
    print(f'{log.default}59.) {log.reset}List computer SyncLAPSPassword privileges')    
    print(f'{log.default}60.) {log.reset}List Domain Admin sessions')
    print(f'{log.default}61.) {log.reset}List Enterprise Admin sessions')
    print(f'{log.default}62.) {log.reset}List all users')
    print(f'{log.default}63.) {log.reset}List all groups')
    print(f'{log.default}64.) {log.reset}List all computers')
    print(f'{log.default}65.) {log.reset}List all enabled computers')
    print(f'{log.default}66.) {log.reset}List all disabled computers')
    print(f'{log.default}67.) {log.reset}List all Domain Controllers')
    print(f'{log.default}68.) {log.reset}List all Domain Controllers OSs')
    print(f'{log.default}69.) {log.reset}List all user shortest paths to Domain Controllers')
    print(f'{log.default}70.) {log.reset}List all group shortest paths to Domain Controllers')
    print(f'{log.default}71.) {log.reset}List all computer shortest paths to Domain Controllers')
    print(f'{log.default}72.) {log.reset}List all users that don\'t require a password')
    print(f'{log.default}73.) {log.reset}List user Constrained Delegation')
    print(f'{log.default}74.) {log.reset}List group Constrained Delegation')
    print(f'{log.default}75.) {log.reset}List computer Constrained Delegation')
    print(f'{log.default}76.) {log.reset}List all GPOs')
    print(f'{log.default}77.) {log.reset}List all domains')
    print(f'{log.default}78.) {log.reset}List all domain trusts')
    print(f'{log.default}79.) {log.reset}List computers with LAPS enabled')
    print(f'{log.default}80.) {log.reset}List computers with LAPS disabled')
    print(f'{log.default}81.) {log.reset}List potential passwords in descriptions')
    print(f'{log.default}82.) {log.reset}List all high-value users')
    print(f'{log.default}83.) {log.reset}List all sensitive users')
    print(f'{log.default}84.) {log.reset}List all users with an admin count')
    print(f'{log.default}85.) {log.reset}List all groups with an admin count')
    print(f'{log.default}86.) {log.reset}List all computers with an admin count')
    print(f'{log.default}87.) {log.reset}List all user ReadGMSAPassword privileges')
    print(f'{log.default}88.) {log.reset}List all group ReadGMSAPassword privileges')
    print(f'{log.default}89.) {log.reset}List all computer ReadGMSAPassword privileges')
    print(f'{log.default}90.) {log.reset}List all user DCSync privileges')
    print(f'{log.default}91.) {log.reset}List all group DCSync privileges')
    print(f'{log.default}92.) {log.reset}List all computer DCSync privileges')
    print(f'{log.default}93.) {log.reset}List all DCSync privileges')
    print(f'{log.default}94.) {log.reset}List all user ForceChangePassword privileges')
    print(f'{log.default}95.) {log.reset}List all group ForceChangePassword privileges')
    print(f'{log.default}96.) {log.reset}List all computer ForceChangePassword privileges')
    print(f'{log.default}97.) {log.reset}List all user AddMember privileges')
    print(f'{log.default}98.) {log.reset}List all group AddMember privileges')
    print(f'{log.default}99.) {log.reset}List all computer AddMember privileges')
    print(f'{log.default}100.) {log.reset}List all user AddSelf privileges')
    print(f'{log.default}101.) {log.reset}List all group AddSelf privileges')
    print(f'{log.default}102.) {log.reset}List all computer AddSelf privileges')
    print(f'{log.default}103.) {log.reset}List all user SQLAdmin privileges')
    print(f'{log.default}104.) {log.reset}List all group SQLAdmin privileges')
    print(f'{log.default}105.) {log.reset}List all computer SQLAdmin privileges')
    print(f'{log.default}106.) {log.reset}List all user CanPSRemote privileges')
    print(f'{log.default}107.) {log.reset}List all group CanPSRemote privileges')
    print(f'{log.default}108.) {log.reset}List all computer CanPSRemote privileges')
    print(f'{log.default}109.) {log.reset}List all user ExecuteDCOM privileges')
    print(f'{log.default}110.) {log.reset}List all group ExecuteDCOM privileges')
    print(f'{log.default}111.) {log.reset}List all computer ExecuteDCOM privileges')
    print(f'{log.default}112.) {log.reset}List all user AllowedToAct privileges')
    print(f'{log.default}113.) {log.reset}List all group AllowedToAct privileges')
    print(f'{log.default}114.) {log.reset}List all computer AllowedToAct privileges')
    print(f'{log.default}115.) {log.reset}List all user Owns privileges')
    print(f'{log.default}116.) {log.reset}List all group Owns privileges')
    print(f'{log.default}117.) {log.reset}List all computer Owns privileges')
    print(f'{log.default}118.) {log.reset}List all user AllExtendedRights privileges')
    print(f'{log.default}119.) {log.reset}List all group AllExtendedRights privileges')
    print(f'{log.default}120.) {log.reset}List all computer AllExtendedRights privileges')
    print(f'{log.default}121.) {log.reset}List all user memberships')
    print(f'{log.default}122.) {log.reset}List all group memberships')
    print(f'{log.default}123.) {log.reset}List all computer memberships')
    print(f'{log.default}124.) {log.reset}List all user AddKeyCredentialLink privileges')
    print(f'{log.default}125.) {log.reset}List all group AddKeyCredentialLink privileges')
    print(f'{log.default}126.) {log.reset}List all computer AddKeyCredentialLink privileges')
    print(f'{log.default}127.) {log.reset}List all user GenericAll privileges')
    print(f'{log.default}128.) {log.reset}List all group GenericAll privileges')
    print(f'{log.default}129.) {log.reset}List all computer GenericAll privileges')
    print(f'{log.default}130.) {log.reset}List all user WriteDacl privileges')
    print(f'{log.default}131.) {log.reset}List all group WriteDacl privileges')
    print(f'{log.default}132.) {log.reset}List all computer WriteDacl privileges')
    print(f'{log.default}133.) {log.reset}List all user WriteOwner privileges')
    print(f'{log.default}134.) {log.reset}List all group WriteOwner privileges')
    print(f'{log.default}135.) {log.reset}List all computer WriteOwner privileges')
    print(f'{log.default}136.) {log.reset}List all user GenericWrite privileges')
    print(f'{log.default}137.) {log.reset}List all group GenericWrite privileges')
    print(f'{log.default}138.) {log.reset}List all computer GenericWrite privileges')
    print(f'{log.default}139.) {log.reset}List groups containing "svc/service"')
    print(f'{log.default}140.) {log.reset}List all user descriptions')
    print(f'{log.default}141.) {log.reset}List all group descriptions')
    print(f'{log.default}142.) {log.reset}List all emails')
    print(f'{log.default}143.) {log.reset}List all OUs')
    print(f'{log.default}144.) {log.reset}List all Containers')
    print(f'{log.default}145.) {log.reset}List all Domains')
    print(f'{log.default}146.) {log.reset}List all Domains functional level')
    print(f'{log.default}147.) {log.reset}List all object control over OUs')
    print(f'{log.default}148.) {log.reset}List all object control over Containers')
    print(f'{log.default}149.) {log.reset}List all object control over GPOs')
    print(f'{log.default}150.) {log.reset}List all GP Links')
    print(f'{log.default}151.) {log.reset}List all user privileges')
    print(f'{log.default}152.) {log.reset}List all group privileges')
    print(f'{log.default}153.) {log.reset}List all computer privileges')


def print_user_list():
    print(f'{log.default}User-Specific Cyphers{log.reset}')
    print(f'{log.default}154.) {log.reset}List this user\'s RDP privileges')
    print(f'{log.default}155.) {log.reset}List this user\'s group-delegated RDP privileges')
    print(f'{log.default}156.) {log.reset}List this user\'s AdminTo privileges')
    print(f'{log.default}157.) {log.reset}List this user\'s group-delegated AdminTo privileges')
    print(f'{log.default}158.) {log.reset}List this user\'s sessions')
    print(f'{log.default}159.) {log.reset}List this user\'s ReadLAPSPassword privileges')
    print(f'{log.default}160.) {log.reset}List this user\'s SyncLAPSPassword privileges')
    print(f'{log.default}161.) {log.reset}List this user\'s ReadGMSAPassword privileges')
    print(f'{log.default}162.) {log.reset}List this user\'s Constrained Delegation privileges')
    print(f'{log.default}163.) {log.reset}List this user\'s ForceChangePassword privileges')
    print(f'{log.default}164.) {log.reset}List this user\'s AddMember privileges')
    print(f'{log.default}165.) {log.reset}List this user\'s AddSelf privileges')
    print(f'{log.default}166.) {log.reset}List this user\'s SQLAdmin privileges')
    print(f'{log.default}167.) {log.reset}List this user\'s CanPSRemote privileges')
    print(f'{log.default}168.) {log.reset}List this user\'s ExecuteDCOM privileges')
    print(f'{log.default}169.) {log.reset}List this user\'s AllowedToAct privileges')
    print(f'{log.default}170.) {log.reset}List this user\'s Owns privileges')
    print(f'{log.default}171.) {log.reset}List this user\'s AllExtendedRights privileges')
    print(f'{log.default}172.) {log.reset}List this user\'s AddKeyCredentialLink privileges')
    print(f'{log.default}173.) {log.reset}List this user\'s GenericAll privileges')
    print(f'{log.default}174.) {log.reset}List this user\'s WriteDacl privileges')
    print(f'{log.default}175.) {log.reset}List this user\'s WriteOwner privileges')
    print(f'{log.default}176.) {log.reset}List this users\'s GenericWrite privileges')
    print(f'{log.default}177.) {log.reset}List this users\'s description')
    print(f'{log.default}178.) {log.reset}List this users\'s email')
    print(f'{log.default}179.) {log.reset}List this users\'s group memberships')
    print(f'{log.default}180.) {log.reset}List if this users\'s AS-REP roastable')
    print(f'{log.default}181.) {log.reset}List if this users\'s kerberoastable')
    print(f'{log.default}182.) {log.reset}List all privileges for this user')
    print(f'{log.default}183.) {log.reset}List all group-delegated privileges for this user')
    print(f'{log.default}184.) {log.reset}List all shortest paths to high-value targets for this user')
    print(f'{log.default}185.) {log.reset}List all shortest paths to Domain Admins for this user')
    print(f'{log.default}186.) {log.reset}List all shortest paths to Enterprise Admins for this user')
    print(f'{log.default}187.) {log.reset}List all shortest paths to Domain Controllers for this user')
    print(f'{log.default}188.) {log.reset}List all shortest paths to Exchange groups for this user')
    print(f'{log.default}189.) {log.reset}List all shortest paths to admin groups for this user')
    print(f'{log.default}190.) {log.reset}List all shortest paths to sql groups for this user')
    print(f'{log.default}191.) {log.reset}List all shortest paths to web groups for this user')
    print(f'{log.default}192.) {log.reset}List all shortest paths to service groups for this user')
    print(f'{log.default}193.) {log.reset}List all shortest paths to this user')


def print_group_list():
    print(f'{log.default}Group-Specific Cyphers{log.reset}')
    print(f'{log.default}194.) {log.reset}List this group\'s RDP privileges')
    print(f'{log.default}195.) {log.reset}List this group\'s group-delegated RDP privileges')
    print(f'{log.default}196.) {log.reset}List this group\'s AdminTo privileges')
    print(f'{log.default}197.) {log.reset}List this group\'s group-delegated AdminTo privileges')
    print(f'{log.default}198.) {log.reset}List this group\'s ReadLAPSPassword privileges')
    print(f'{log.default}199.) {log.reset}List this group\'s SyncLAPSPassword privileges')
    print(f'{log.default}200.) {log.reset}List this group\'s ReadGMSAPassword privileges')
    print(f'{log.default}201.) {log.reset}List this group\'s Constrained Delegation privileges')
    print(f'{log.default}202.) {log.reset}List this group\'s ForceChangePassword privileges')
    print(f'{log.default}203.) {log.reset}List this group\'s AddMember privileges')
    print(f'{log.default}204.) {log.reset}List this group\'s AddSelf privileges')
    print(f'{log.default}205.) {log.reset}List this group\'s SQLAdmin privileges')
    print(f'{log.default}206.) {log.reset}List this group\'s CanPSRemote privileges')
    print(f'{log.default}207.) {log.reset}List this group\'s ExecuteDCOM privileges')
    print(f'{log.default}208.) {log.reset}List this group\'s AllowedToAct privileges')
    print(f'{log.default}209.) {log.reset}List this group\'s Owns privileges')
    print(f'{log.default}210.) {log.reset}List this group\'s AllExtendedRights privileges')
    print(f'{log.default}211.) {log.reset}List this group\'s AddKeyCredentialLink privileges')
    print(f'{log.default}212.) {log.reset}List this group\'s GenericAll privileges')
    print(f'{log.default}213.) {log.reset}List this group\'s WriteDacl privileges')
    print(f'{log.default}214.) {log.reset}List this group\'s WriteOwner privileges')
    print(f'{log.default}215.) {log.reset}List this groups\'s GenericWrite privileges')
    print(f'{log.default}216.) {log.reset}List this groups\'s description')
    print(f'{log.default}217.) {log.reset}List this groups\'s group memberships')
    print(f'{log.default}218.) {log.reset}List this groups\'s members')
    print(f'{log.default}219.) {log.reset}List all privileges for this group')
    print(f'{log.default}220.) {log.reset}List all group-delegated privileges for this group')
    print(f'{log.default}221.) {log.reset}List all shortest paths to high-value targets for this group')
    print(f'{log.default}222.) {log.reset}List all shortest paths to Domain Admins for this group')
    print(f'{log.default}223.) {log.reset}List all shortest paths to Enterprise Admins for this group')
    print(f'{log.default}224.) {log.reset}List all shortest paths to Domain Controllers for this group')
    print(f'{log.default}225.) {log.reset}List all shortest paths to Exchange groups for this group')
    print(f'{log.default}226.) {log.reset}List all shortest paths to admin groups for this group')
    print(f'{log.default}227.) {log.reset}List all shortest paths to sql groups for this group')
    print(f'{log.default}228.) {log.reset}List all shortest paths to web groups for this group')
    print(f'{log.default}229.) {log.reset}List all shortest paths to service groups for this group')
    print(f'{log.default}230.) {log.reset}List all shortest paths to this group')


def print_computer_list():
    print(f'{log.default}Computer-Specific Cyphers{log.reset}')
    print(f'{log.default}231.) {log.reset}List this computer\'s AdminTo privileges')
    print(f'{log.default}232.) {log.reset}List this computer\'s group-delegated AdminTo privileges')
    print(f'{log.default}233.) {log.reset}List this computer\'s ReadLAPSPassword privileges')
    print(f'{log.default}234.) {log.reset}List this computer\'s SyncLAPSPassword privileges')
    print(f'{log.default}235.) {log.reset}List this computer\'s ReadGMSAPassword privileges')
    print(f'{log.default}236.) {log.reset}List this computer\'s Constrained Delegation privileges')
    print(f'{log.default}237.) {log.reset}List this computer\'s ForceChangePassword privileges')
    print(f'{log.default}238.) {log.reset}List this computer\'s AddMember privileges')
    print(f'{log.default}239.) {log.reset}List this computer\'s AddSelf privileges')
    print(f'{log.default}240.) {log.reset}List this computer\'s SQLAdmin privileges')
    print(f'{log.default}241.) {log.reset}List this computer\'s CanPSRemote privileges')
    print(f'{log.default}242.) {log.reset}List this computer\'s ExecuteDCOM privileges')
    print(f'{log.default}243.) {log.reset}List this computer\'s AllowedToAct privileges')
    print(f'{log.default}244.) {log.reset}List this computer\'s Owns privileges')
    print(f'{log.default}245.) {log.reset}List this computer\'s AllExtendedRights privileges')
    print(f'{log.default}246.) {log.reset}List this computer\'s AddKeyCredentialLink privileges')
    print(f'{log.default}247.) {log.reset}List this computer\'s GenericAll privileges')
    print(f'{log.default}248.) {log.reset}List this computer\'s WriteDacl privileges')
    print(f'{log.default}249.) {log.reset}List this computer\'s WriteOwner privileges')
    print(f'{log.default}250.) {log.reset}List this computers\'s GenericWrite privileges')
    print(f'{log.default}251.) {log.reset}List this computers\'s group memberships')
    print(f'{log.default}252.) {log.reset}List all privileges for this computer')
    print(f'{log.default}253.) {log.reset}List all group-delegated privileges for this computer')
    print(f'{log.default}254.) {log.reset}List all shortest paths to high-value targets for this computer')
    print(f'{log.default}255.) {log.reset}List all shortest paths to Domain Admins for this computer')
    print(f'{log.default}256.) {log.reset}List all shortest paths to Enterprise Admins for this computer')
    print(f'{log.default}257.) {log.reset}List all shortest paths to Domain Controllers for this computer')
    print(f'{log.default}258.) {log.reset}List all shortest paths to Exchange groups for this computer')
    print(f'{log.default}259.) {log.reset}List all shortest paths to admin groups for this computer')
    print(f'{log.default}260.) {log.reset}List all shortest paths to sql groups for this computer')
    print(f'{log.default}261.) {log.reset}List all shortest paths to web groups for this computer')
    print(f'{log.default}262.) {log.reset}List all shortest paths to service groups for this computer')
    print(f'{log.default}263.) {log.reset}List all shortest paths to this computer')


def print_regex_list():
    print(f'{log.default}Regex-Specific Cyphers{log.reset}')
    print(f'{log.default}264.) {log.reset}Search for groups matching the regex')
    print(f'{log.default}265.) {log.reset}Search for users matching the regex')
    print(f'{log.default}266.) {log.reset}Search for computers matching the regex')
    print(f'{log.default}267.) {log.reset}Search for user descriptions matching the regex')
    print(f'{log.default}268.) {log.reset}Search for group descriptions matching the regex')
    print(f'{log.default}269.) {log.reset}Search for OSs matching the regex')
    print(f'{log.default}270.) {log.reset}Search for GPOs matching the regex')
    print(f'{log.default}271.) {log.reset}Search for Containers matching the regex')
    print(f'{log.default}272.) {log.reset}Search for OUs matching the regex')


def print_all():
    print_general_list()
    print_user_list()
    print_group_list()
    print_computer_list()
    print_regex_list()