# Nom de la librairie à générer
NAME = libasm.a

# Fichiers source en assembleur
SRCS = 	ft_write.s \
		ft_read.s \
		ft_strcmp.s \
		ft_strcpy.s \
		ft_strdup.s \
		ft_strlen.s

# Objets générés
OBJS = $(SRCS:.s=.o)

# Détection du système pour choisir le bon format NASM
UNAME := $(shell uname)

ifeq ($(UNAME), Darwin)
	NASMFLAGS = -f macho64
else
	NASMFLAGS = -f elf64
endif

NASM = nasm

# Compilation des fichiers .s
%.o: %.s
	$(NASM) $(NASMFLAGS) $< -o $@

# Règle all : génère la lib
all: $(NAME)

$(NAME): $(OBJS)
	ar rcs $(NAME) $(OBJS)

# Nettoyage des .o
clean:
	rm -f $(OBJS)

# Nettoyage complet
fclean: clean
	rm -f $(NAME)

# Recompilation complète
re: fclean all

# Compilation bonus (à implémenter + tard)
bonus:
	@echo "Bonus rule ready (fichiers *_bonus.s nécessaires)"

.PHONY: all clean fclean re bonus