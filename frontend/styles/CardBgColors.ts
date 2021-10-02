import { OrganizationType } from "types/WaitingTimeHistories"

const CardBgColor = (OrganizationType: OrganizationType) => {
    switch(OrganizationType){
        case "M":
            return "red.300"
        case "E":
            return "yellow.200"
        case "I":
            return "blue.400"
        case "C":
            return "green.300"
        case "A":
            return "lightBlue"
        case "CLUB":
            return "gray.100"
    }

}

export default CardBgColor