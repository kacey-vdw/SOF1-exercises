import copy


class GameObject:
    """
    class for wooden pieces in game
    """

    def __init__(self, shape, colour):
        """
        initialises GameObject instance

        Args:
            shape: shape of the object
            colour: colour of the object
        """

        self._shape = shape
        self._colour = colour

    @property
    def shape(self):
        """returns shape as property"""
        return self._shape

    @property
    def colour(self):
        """returns _colour as property"""
        return self._colour

    def __eq__(self, other):
        """
        Compares two GameObjects (overrides == operator)

        Args:
            other: the object to compare to

        Returns:
            Returns True or False
        """
        try:  # compare shape and colour of both items
            if self.shape == other.shape and self.colour == other.colour:
                return True
            else:
                return False
        except:  # if compared items are not both GameObjects, false
            return False

    def half_eq(self, other):
        """
        Compares two GameObjects to see if they have same shape OR colour

        Args:
            other: the object to compare to

        Returns:
            Returns True or False
        """
        if self.shape == other.shape or self.colour == other.colour:
            return True
        else:
            return False


class GameCard:
    """
    class for cards in game
    """
    def __init__(self, object1, object2):
        """
        initialises GameCard instance

        Args:
            object1: a GameObject instance
            object2: another GameObject instance
        """
        self._content = [copy.copy(object1), copy.copy(object2)]

    @property
    def content(self):
        """returns contents as property"""
        return copy.deepcopy(self._content)

    def __eq__(self, other):
        """
        Compares two GameCards (overrides == operator)

        Args:
            other: the object to compare to

        Returns:
            Returns True or False
        """
        try:
            for item in self.content:
                if item not in other.content:
                    return False
            return True
        except:  # covers any non-equal objects non comparable
            return False


class CardDeck:
    """
    class for a deck of cards in game
    """
    def __init__(self, objects):
        """
        initialises GameCard instance

        Args:
            objects: a list of GameObject instances

        Raises:
            ValueError: if not 3,4,5 objs or 2 objs have same colour/shape
        """
        if len(objects) > 5 or len(objects) < 3:
            raise ValueError
        else:
            for obj1 in objects:
                for obj2 in objects:
                    if obj1 == obj2:  # if comparing to self, skip
                        break
                    elif obj1.half_eq(obj2):  # if same colour/shape, error
                        raise ValueError

            self.deck = objects

    def generate_deck(self):
        """
        returns a list of valid cards

        Returns:
            A list of valid cards
        """
        valid = []
        colours = []
        shapes = []
        combos = []

        for obj in self.deck:  # makes lists of all colours and shapes
            colours.append(obj.colour)
            shapes.append(obj.shape)

        colours = list(dict.fromkeys(colours))  # remove duplicates
        shapes = list(dict.fromkeys(shapes))

        for clr in colours:  # makes all possible shape/colour combos
            for shp in shapes:
                combos.append(GameObject(shp, clr))

        for comb1 in combos:  # makes all possible card combos
            for comb2 in combos:
                if comb1 == comb2:  # ignore pair of exact same object
                    continue
                else:
                    valid.append(GameCard(comb1, comb2))

        return valid
