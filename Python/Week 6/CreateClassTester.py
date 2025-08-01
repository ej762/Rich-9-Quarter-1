import CreateClass

movies =["Jurrasic world","Fnaf","Superman" ]
games =["2k","NCAA","Fortass"]
EjCollection = CreateClass.Collection(movies, games)

EjCollection.SetFavGame("NCAA")
EjCollection.SetFavMovie("Superman")
EjCollection.DisplayCollection()