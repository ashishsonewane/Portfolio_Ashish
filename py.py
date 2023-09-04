
class search_filter(APIView):
    def post(self, request, format=None):
        try:
            # user_id = request.GET.get("user_id",None)
            user_id = request.data.get("user_id")
            # Residential and Commercial======(id)
            propertylistingtypeobj = request.data.get('property_listing')
            if Propertylisting_type.objects.filter(id=propertylistingtypeobj):
                listingtypeob = Propertylisting_type.objects.get(
                    id=propertylistingtypeobj)
            else:
                listingtypeob = None
            # rent , buy , sales, leasing, etc.========(id)
            categoryid = request.data.get('category')
            if Property_Listing_Type.objects.filter(id=categoryid):
                categoryobj = Property_Listing_Type.objects.get(id=categoryid)
            else:

                categoryobj = None

            # Main Category (id)

            typeid = request.data.get('type')

            if Property_Main_Category.objects.filter(id=typeid):

                tyepobj = Property_Main_Category.objects.get(id=typeid)

            else:

                tyepobj = None

            # Area Master

            areaid = request.data.get('area')

            if AreaMaster.objects.filter(id=areaid):

                areaobj = AreaMaster.objects.get(id=areaid)

            else:

                areaobj = None

            # City Master

            cityid = request.data.get('city')

            if CityMaster.objects.filter(id=cityid):

                cityobj = CityMaster.objects.get(id=cityid)

            else:

                cityobj = None

            # State Master

            stateid = request.data.get('state')

            if StateMaster.objects.filter(id=stateid):

                stateobj = StateMaster.objects.get(id=stateid)

            else:

                stateobj = None

            # Country Master

            countryid = request.data.get('country')

            if CountryMaster.objects.filter(id=countryid):

                countryobj = CountryMaster.objects.get(id=countryid)

            else:

                countryobj = None

            pricemin = request.data.get('pricemin')

            pricemax = request.data.get('pricemax')

            squftmin = request.data.get('Squft_min')

            squftmax = request.data.get('Squft_max')

            filterobj = request.data['filter_obj']

            if listingtypeob is not None and categoryobj is not None:

                if tyepobj != None:

                    if tyepobj.Main_category == "Leisure":

                        Sub_category = request.data.get('Sub_category')

                        propertysubcategoryobj = Property_Sub_Category.objects.get(
                            id=Sub_category)

                        propertyobj = Property_Detail.objects.filter(property_listing_type=listingtypeob.id).filter(
                            propertylisting_type=categoryobj.id).filter(property_main_category=tyepobj).filter(property_sub_category=propertysubcategoryobj)

                    else:

                        propertyobj = Property_Detail.objects.filter(property_listing_type=listingtypeob.id).filter(
                            propertylisting_type=categoryobj.id).filter(property_main_category=tyepobj)

                else:

                    propertyobj = Property_Detail.objects.filter(
                        property_listing_type=listingtypeob.id).filter(propertylisting_type=categoryobj.id)

                if filterobj == False:

                    # Area

                    if areaobj != None and cityobj != None and stateobj != None and countryobj != None:

                        propertyobj = propertyobj.filter(
                            property_area=areaobj.id)

                        if pricemin != None or pricemax != None:

                            propertyobj = propertyobj.filter(property_listing_amount__gte=pricemin).filter(
                                property_listing_amount__lte=pricemax)

                    # City

                    elif areaobj == None and cityobj != None and stateobj != None and countryobj != None:

                        propertyobj = propertyobj.filter(
                            property_city=cityobj.id)

                        if pricemin != None or pricemax != None:

                            propertyobj = propertyobj.filter(property_listing_amount__gte=pricemin).filter(
                                property_listing_amount__lte=pricemax)

                    # State

                    elif areaobj == None and cityobj == None and stateobj != None and countryobj != None:

                        propertyobj = propertyobj.filter(
                            property_state=stateobj.id)

                        if pricemin != None or pricemax != None:

                            propertyobj = propertyobj.filter(property_listing_amount__gte=pricemin).filter(
                                property_listing_amount__lte=pricemax)

                    # Country

                    elif areaobj == None and cityobj == None and stateobj == None and countryobj != None:

                        state_obj = StateMaster.objects.filter(
                            country_master=countryobj.id).values_list('id', flat=True)

                        propertyobj = propertyobj.filter(
                            property_state__in=state_obj)

                        if pricemin != None or pricemax != None:

                            propertyobj = propertyobj.filter(property_listing_amount__gte=pricemin).filter(
                                property_listing_amount__lte=pricemax)

                    # # Else

                    else:

                        if pricemin != None or pricemax != None:

                            propertyobj = propertyobj.filter(property_listing_amount__gte=pricemin).filter(
                                property_listing_amount__lte=pricemax)

                else:

                    if listingtypeob.property_listing_name == 'Residential':

                        bedrooms = request.data.get('Bedrooms')

                        bathrooms = request.data.get('Bathrooms')

                        amenities = request.data.get('Amenities_filter')

                        # Area

                        if areaobj != None and cityobj != None and stateobj != None and countryobj != None:

                            propertyobj = propertyobj.filter(
                                property_area=areaobj.id)

                            if pricemin != None or pricemax != None:

                                propertyobj = propertyobj.filter(property_listing_amount__gte=pricemin).filter(
                                    property_listing_amount__lte=pricemax)

                            if squftmin != None or squftmax != None:

                                propertyobj = propertyobj.filter(
                                    Square_sqft__gte=squftmin).filter(Square_sqft__lte=squftmax)

                        # City

                        elif areaobj == None and cityobj != None and stateobj != None and countryobj != None:

                            propertyobj = propertyobj.filter(
                                property_city=cityobj.id)

                            if pricemin != None or pricemax != None:

                                propertyobj = propertyobj.filter(property_listing_amount__gte=pricemin).filter(
                                    property_listing_amount__lte=pricemax)

                            if squftmin != None or squftmax != None:

                                propertyobj = propertyobj.filter(
                                    Square_sqft__gte=squftmin).filter(Square_sqft__lte=squftmax)

                        # State

                        elif areaobj == None and cityobj == None and stateobj != None and countryobj != None:

                            propertyobj = propertyobj.filter(
                                property_state__in=stateobj.id)

                            if pricemin != None or pricemax != None:

                                propertyobj = propertyobj.filter(property_listing_amount__gte=pricemin).filter(
                                    property_listing_amount__lte=pricemax)

                            if squftmin != None or squftmax != None:

                                propertyobj = propertyobj.filter(
                                    Square_sqft__gte=squftmin).filter(Square_sqft__lte=squftmax)

                        # Country

                        elif areaobj == None and cityobj == None and stateobj == None and countryobj != None:

                            state_obj = StateMaster.objects.filter(
                                country_master=countryobj.id)

                            propertyobj = propertyobj.filter(
                                property_state__in=state_obj)

                            if pricemin != None or pricemax != None:

                                propertyobj = propertyobj.filter(property_listing_amount__gte=pricemin).filter(
                                    property_listing_amount__lte=pricemax)

                            if squftmin != None or squftmax != None:

                                propertyobj = propertyobj.filter(
                                    Square_sqft__gte=squftmin).filter(Square_sqft__lte=squftmax)

                        # Else

                        else:

                            if pricemin != None or pricemax != None:

                                propertyobj = propertyobj.filter(property_listing_amount__gte=pricemin).filter(
                                    property_listing_amount__lte=pricemax)

                            if squftmin != None or squftmax != None:

                                propertyobj = propertyobj.filter(
                                    Square_sqft__gte=squftmin).filter(Square_sqft__lte=squftmax)

                        if bedrooms != None:

                            propertyobj = propertyobj.filter(
                                Bedrooms__gte=bedrooms)

                            print(propertyobj)

                        if bathrooms != None:

                            propertyobj = propertyobj.filter(
                                Bathrooms__gte=bathrooms)

                        if amenities != None:

                            property_detail_obj_id = propertyobj.values_list(
                                'id', flat=True)

                            property_obj = Property_Amenities.objects.filter(
                                property_details__in=property_detail_obj_id).filter(amenites_master__in=amenities)

                        else:

                            property_obj = None

                    elif listingtypeob.property_listing_name == 'Commercial':

                        unit = request.POST.get('units')

                        room = request.POST.get('room')

                        block = request.POST.get('block')

                        lot = request.POST.get('lot')

                        zone = request.POST.get('Zone')

                        lot_dimension = request.POST.get('lot_diamensions')

                        building_dimension = request.POST.get(
                            'building_diamensions')

                        stories = request.POST.get('stories')

                        far = request.POST.get('far')

                        assessment = request.POST.get('Assessment')

                        annual_taxes = request.POST.get('Annual_Taxes')

                        available_air_rights = request.POST.get(
                            'Available_Air_Rights')

                        # Area

                        if areaobj != None and cityobj != None and stateobj != None and countryobj != None:

                            propertyobj = propertyobj.filter(
                                property_area=areaobj.id)

                            if pricemin != None or pricemax != None:

                                propertyobj = propertyobj.filter(property_listing_amount__gte=pricemin).filter(
                                    property_listing_amount__lte=pricemax)

                            if squftmin != None or squftmax != None:

                                propertyobj = propertyobj.filter(
                                    Square_sqft__gte=squftmin).filter(Square_sqft__lte=squftmax)

                        # City

                        elif areaobj == None and cityobj != None and stateobj != None and countryobj != None:

                            propertyobj = propertyobj.filter(
                                property_city=cityobj.id)

                            if pricemin != None or pricemax != None:

                                propertyobj = propertyobj.filter(property_listing_amount__gte=pricemin).filter(
                                    property_listing_amount__lte=pricemax)

                            if squftmin != None or squftmax != None:

                                propertyobj = propertyobj.filter(
                                    Square_sqft__gte=squftmin).filter(Square_sqft__lte=squftmax)

                        # State

                        elif areaobj == None and cityobj == None and stateobj != None and countryobj != None:

                            propertyobj = propertyobj.filter(
                                property_state__in=stateobj.id)

                            if pricemin != None or pricemax != None:

                                propertyobj = propertyobj.filter(property_listing_amount__gte=pricemin).filter(
                                    property_listing_amount__lte=pricemax)

                            if squftmin != None or squftmax != None:

                                propertyobj = propertyobj.filter(
                                    Square_sqft__gte=squftmin).filter(Square_sqft__lte=squftmax)

                        # Country

                        elif areaobj == None and cityobj == None and stateobj == None and countryobj != None:

                            state_obj = StateMaster.objects.filter(
                                country_master=countryobj.id)

                            propertyobj = propertyobj.filter(
                                property_state__in=state_obj)

                            if pricemin != None or pricemax != None:

                                propertyobj = propertyobj.filter(property_listing_amount__gte=pricemin).filter(
                                    property_listing_amount__lte=pricemax)

                            if squftmin != None or squftmax != None:

                                propertyobj = propertyobj.filter(
                                    Square_sqft__gte=squftmin).filter(Square_sqft__lte=squftmax)

                        # Else

                        else:

                            if pricemin != None or pricemax != None:

                                propertyobj = propertyobj.filter(property_listing_amount__gte=pricemin).filter(
                                    property_listing_amount__lte=pricemax)

                            if squftmin != None or squftmax != None:

                                propertyobj = propertyobj.filter(
                                    Square_sqft__gte=squftmin).filter(Square_sqft__lte=squftmax)

                        if unit != None:

                            propertyobj = propertyobj.filter(Units__gte=unit)

                        if room != None:

                            propertyobj = propertyobj.filter(Rooms__gte=room)

                        if block != None:

                            propertyobj = propertyobj.filter(Block__gte=block)

                        if lot != None:

                            propertyobj = propertyobj.filter(Lot__gte=lot)

                        if zone != None:

                            propertyobj = propertyobj.filter(Zone__gte=zone)

                        if lot_dimension != None:

                            propertyobj = propertyobj.filter(
                                Lot_Dimensions__gte=lot_dimension)

                        if building_dimension != None:

                            propertyobj = propertyobj.filter(
                                Building_Dimension__gte=building_dimension)

                        if stories != None:

                            propertyobj = propertyobj.filter(
                                Stories__gte=stories)

                        if far != None:

                            propertyobj = propertyobj.filter(FAR__gte=far)

                        if assessment != None:

                            propertyobj = propertyobj.filter(
                                Assessment__gte=assessment)

                        if annual_taxes != None:

                            propertyobj = propertyobj.filter(
                                Annual_Taxes__gte=annual_taxes)

                        if available_air_rights != None:

                            propertyobj = propertyobj.filter(
                                Available_Air_Rights__gte=available_air_rights)

                cityidnb = []

                for i in propertyobj:

                    if i.property_city.id not in cityidnb:

                        cityidnb.append(i.property_city.id)

                    else:

                        pass

                areaidnb = AreaMaster.objects.filter(city_master__in=cityidnb)

                nbspuser = []

                for areaobj in areaidnb:

                    neighbourhood_spicialityobj = Nb_specality_area.objects.filter(
                        area_id__icontains=areaobj.id, is_verified="Approve")

                    for j in neighbourhood_spicialityobj:

                        neighbourhood_spicialityid = Nb_specality_area.objects.get(
                            id=j.id)

                        if neighbourhood_spicialityid.user.id not in nbspuser:

                            nbspuser.append(neighbourhood_spicialityid.user.id)

                        else:

                            pass

                userobj = User.objects.filter(id__in=nbspuser)

                usertypeobj = UserType.objects.filter(user__in=userobj)

                userprofileobj = UserProfile.objects.filter(
                    user_type__in=usertypeobj)

                nbserializer = NeighborAvaliableProfileSerializer(
                    userprofileobj, many=True)

                paginator = MyPagination()

                paginated_queryset = paginator.paginate_queryset(
                    propertyobj, request)

                serializer = PropertySerializer(paginated_queryset, context={
                                                'user_id': user_id}, many=True)

                # serializer1=PropertyAmenitiesSerializer(property_obj, many=True)

                if serializer.data:

                    # if serializer1.data:

                    # return Response(util.success(self,[serializer.data,serializer1.data]))

                    if areaobj:

                        return Response(util.success(self, {"porperty": serializer.data, "page": 2, "Neighborhood": nbserializer.data}))

                    else:

                        return Response(util.success(self, {"porperty": serializer.data, "page": 1, "Neighborhood": nbserializer.data}))

                else:

                    return Response(util.error(self, 'No Data Found'))

            else:

                return Response(util.error(self, "property_listing, category is required"))

        except Exception as e:

            return Response(util.error(self, str(e)))
