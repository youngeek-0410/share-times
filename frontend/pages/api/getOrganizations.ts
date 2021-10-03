import { Organization } from "types/WaitingTimeHistories"

const getOrganizations = async(): Promise<Organization[]> => {
    const res = await fetch('http://localhost/api/organization')
    return res.json()
}

export default getOrganizations